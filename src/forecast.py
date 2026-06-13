import pandas as pd

from sklearn.linear_model import LinearRegression


def train_model(df):

    X_raw = df[
        [
            'oze_share',
            'inflation',
            'gdp_per_capita',
            'year',
            'country'
        ]
    ]

    X = pd.get_dummies(
        X_raw,
        columns=['country'],
        drop_first=True
    )

    y = df['energy_price']

    model = LinearRegression()

    model.fit(X, y)

    return model, X.columns


def predict_country(
    country_name,
    df,
    years=5
):

    model, feature_columns = train_model(df)

    country_history = (
        df[
            df['country'] == country_name
        ]
        .sort_values('year')
    )

    last_row = country_history.iloc[-1]

    current_oze = last_row['oze_share']
    current_inflation = last_row['inflation']
    current_gdp = last_row['gdp_per_capita']

    oze_growth = (
        country_history['oze_share']
        .diff()
        .mean()
    )

    inflation_growth = (
        country_history['inflation']
        .diff()
        .mean()
    )

    gdp_growth = (
        country_history['gdp_per_capita']
        .diff()
        .mean()
    )

    predictions = []

    current_year = int(
        last_row['year']
    )

    for i in range(years):

        current_year += 1

        current_oze += oze_growth
        current_inflation += inflation_growth
        current_gdp += gdp_growth

        X_future = pd.DataFrame(
            0,
            index=[0],
            columns=feature_columns
        )

        X_future['year'] = current_year

        X_future['oze_share'] = current_oze

        X_future['inflation'] = current_inflation

        X_future['gdp_per_capita'] = current_gdp

        country_column = (
            f'country_{country_name}'
        )

        if country_column in X_future.columns:

            X_future[
                country_column
            ] = 1

        predicted_price = (
            model
            .predict(X_future)[0]
        )

        predictions.append(
            {
                "year": current_year,
                "predicted_energy_price": predicted_price,
                "predicted_oze_share": current_oze,
                "predicted_inflation": current_inflation,
                "predicted_gdp_per_capita": current_gdp
            }
        )

    return pd.DataFrame(
        predictions
    )