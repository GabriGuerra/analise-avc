import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('imagens', exist_ok=True)

def gerar_visualizacoes_gerais(df):
    sns.histplot(data=df, x='age', hue='stroke', kde=True)
    plt.title('Distribuição de Idade por Ocorrência de AVC')
    plt.savefig('imagens/grafico_idade_avc.png', dpi=300)
    plt.clf()

    sns.boxplot(x='stroke', y='avg_glucose_level', data=df)
    plt.title('Boxplot de Glicemia por Status de AVC')
    plt.savefig('imagens/boxplot_glicemia.png', dpi=300)
    plt.clf()

    sns.histplot(data=df, x='avg_glucose_level', hue='stroke', kde=True)
    plt.title('Distribuição de Glicemia por Status de AVC')
    plt.savefig('imagens/histograma_glicemia.png', dpi=300)
    plt.clf()

    sns.boxplot(data=df[['avg_glucose_level', 'bmi']])
    plt.title('Boxplot de Glicemia e IMC')
    plt.savefig('imagens/boxplot_glicemia_bmi.png', dpi=300)
    plt.clf()