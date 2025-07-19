import matplotlib.pyplot as plt
import seaborn as sns

def gerar_heatmap_correlacao(df):
    corr = df.drop(columns=['id', 'faixa_etaria']).corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.3,
                linecolor='white', square=True, cbar=False, annot_kws={"size": 8})
    plt.title('Matriz de Correlação entre Variáveis Numéricas')
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.yticks(rotation=0, fontsize=9)
    plt.tight_layout()
    plt.savefig('imagens/heatmap_correlacao.png', dpi=300)
    plt.clf()