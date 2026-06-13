import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


def get_model_info(df):

    # =====================================
    # Dane bez kryzysu
    # =====================================

    df = df[df["year"] <= 2020]

    feature_cols = [
        "oze_share",
        "year",
        "country",
        "inflation",
        "gdp_per_capita"
    ]

    X_raw = df[feature_cols]

    X = pd.get_dummies(
        X_raw,
        columns=["country"],
        drop_first=True
    )

    y = df["energy_price"]

    # =====================================
    # 50 losowych podziałów train/test
    # =====================================

    r2_scores = []
    mae_scores = []
    rmse_scores = []

    for seed in range(50):

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=seed
        )

        model = LinearRegression()

        model.fit(
            X_train,
            y_train
        )

        y_pred = model.predict(
            X_test
        )

        r2_scores.append(
            r2_score(
                y_test,
                y_pred
            )
        )

        mae_scores.append(
            mean_absolute_error(
                y_test,
                y_pred
            )
        )

        rmse_scores.append(
            np.sqrt(
                mean_squared_error(
                    y_test,
                    y_pred
                )
            )
        )

    # =====================================
    # Standaryzowane współczynniki
    # =====================================

    X_scaled = X.copy()

    numeric_cols = [
        "oze_share",
        "inflation",
        "gdp_per_capita",
        "year"
    ]

    scaler = StandardScaler()

    X_scaled[numeric_cols] = scaler.fit_transform(
        X_scaled[numeric_cols]
    )

    model_std = LinearRegression()

    model_std.fit(
        X_scaled,
        y
    )

    coeff_df = pd.DataFrame(
        {
            "Feature": X_scaled.columns,
            "Coefficient": model_std.coef_
        }
    )


    # =====================================
    # Tylko główne zmienne
    # =====================================

    coeff_df = coeff_df[
        coeff_df["Feature"].isin(
            [
                "oze_share",
                "inflation",
                "gdp_per_capita",
                "year"
            ]
        )
    ].copy()

    # =====================================
    # Procentowy udział
    # =====================================

    coeff_df["Abs"] = (
        coeff_df["Coefficient"]
        .abs()
    )

    total = coeff_df["Abs"].sum()

    coeff_df["Percent"] = (
        coeff_df["Abs"]
        / total
        * 100
    )

    coeff_df = coeff_df.sort_values(
        "Percent",
        ascending=True
    )

    return {

        "r2_mean": np.mean(r2_scores),
        "r2_std": np.std(r2_scores),
        "r2_min": np.min(r2_scores),
        "r2_max": np.max(r2_scores),

        "mae_mean": np.mean(mae_scores),

        "rmse_mean": np.mean(rmse_scores),

        "coefficients": coeff_df
    }