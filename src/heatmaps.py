import matplotlib.pyplot as plt
import seaborn as sns


def create_heatmap(df, column_name, title, cmap,annot=True,
    fmt=".1f"):

    heatmap_data = (
        df
        .pivot_table(
            index='country',
            columns='year',
            values=column_name
        )
    )

    # Sortowanie po średniej wartości
    heatmap_data = heatmap_data.loc[
        heatmap_data.mean(axis=1)
        .sort_values(ascending=False)
        .index
    ]

    fig, ax = plt.subplots(
        figsize=(14, 10)
    )

    sns.heatmap(
        heatmap_data,
        cmap=cmap,
        ax=ax,
        annot=annot,
        fmt = fmt
    )

    ax.set_title(title)

    plt.tight_layout()

    return fig