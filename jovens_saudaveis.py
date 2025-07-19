import matplotlib.pyplot as plt
import seaborn as sns

def analisar_jovens_saudaveis(df):
    jovens_saudaveis = df[(df['faixa_etaria'] == 'jovem') &
                          (df['hypertension'] == 0) &
                          (df['heart_disease'] == 0)]
    print("\nCasos de AVC entre jovens sem comorbidades:")
    print(jovens_saudaveis['stroke'].value_counts())
    print(f"Total: {len(jovens_saudaveis)}")

    sns.scatterplot(data=jovens_saudaveis, x='avg_glucose_level', y='bmi', hue='stroke')
    plt.title('Jovens sem Comorbidades - Glicemia vs IMC')
    plt.savefig('imagens/dispersao_jovens_saudaveis.png', dpi=300)
    plt.clf()