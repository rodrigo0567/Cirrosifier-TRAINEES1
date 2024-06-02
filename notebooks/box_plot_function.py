import matplotlib.pyplot as plt 
import pandas as pd
def plot_boxplots(df:pd.DataFrame = None, serie_categoria:pd.Series = None, 
                  serie_alvo:pd.Series = None, min:int=0, max:int=0, legend:bool = True):

    fig, ax = plt.subplots()
    ax2 = ax.twinx()

    if (df is not None) and (serie_categoria is None) or (serie_alvo is None):
        ax.boxplot(
        df,
        labels = df.columns,
        vert=False
        )
        return ax

    else:

        if ((min != 0) and (max != 0)):
            ax2.axvspan(
                xmin=min,
                xmax=max,
                color='lightgreen',
                alpha=0.25,
                label=f'Intervalo Adequado ({min}-{max})'
                )
            if legend:
                plt.legend()

        ax2.set_yticklabels([])
        ax2.set_ylim(ax.get_ylim())

        if (serie_categoria is None) or (serie_categoria.empty):
            ax.boxplot(
                serie_alvo,
                labels=[serie_alvo.name],
                vert=False
            )
            plt.title(f'Distribuição de {serie_alvo.name}')

            return ax

        categoria_name = serie_categoria.name
        alvo_name = serie_alvo.name
        map = {categoria: i for i, categoria in enumerate(serie_categoria.unique())}

        for categoria in serie_categoria.unique():
            ax.boxplot(
                df[df[categoria_name] == categoria][alvo_name],
                positions=[map[categoria]],
                labels=[categoria],
                vert=False
            )

        plt.title(f'Distribuição de {alvo_name} por {categoria_name}')

        return ax