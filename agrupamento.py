import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def executar_agrupamento(df):
    scaler = StandardScaler()
    cluster_data = scaler.fit_transform(df[['age', 'avg_glucose_level', 'bmi']])
    sse = []
    for k in range(1, 10):
        km = KMeans(n_clusters=k, random_state=0)
        km.fit(cluster_data)
        sse.append(km.inertia_)
    plt.plot(range(1, 10), sse, marker='o')
    plt.title('Elbow Method para Definição do Número de Clusters')
    plt.savefig('imagens/elbow_method.png', dpi=300)
    plt.clf()

    km = KMeans(n_clusters=3, random_state=0)
    df['cluster'] = km.fit_predict(cluster_data)
    print("\nPacientes por cluster:")
    print(df['cluster'].value_counts())
    cluster_avc = df.groupby('cluster')['stroke'].mean().round(3) * 100
    print("\n% AVC por Cluster:")
    print(cluster_avc.to_frame(name='% AVC'))

    sns.scatterplot(x='age', y='avg_glucose_level', hue='cluster', data=df, palette='Set1')
    plt.title('Agrupamento por Idade e Glicemia')
    plt.savefig('imagens/dispersao_clusters.png', dpi=300)
    plt.clf()