import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from scipy import stats

os.makedirs('imagens', exist_ok=True)

df = pd.read_csv('healthcare-dataset-stroke-data.csv')

print("\nInformações do DataFrame:")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe())

df['bmi'] = df['bmi'].fillna(df['bmi'].median())
df['smoking_status'] = df['smoking_status'].replace('Unknown', np.nan)
df['smoking_status'] = df['smoking_status'].fillna('never smoked')
df.drop_duplicates(inplace=True)

le = LabelEncoder()
for col in ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']:
    df[col] = le.fit_transform(df[col])

df['faixa_etaria'] = pd.cut(df['age'], bins=[0, 30, 60, 100], labels=['jovem', 'adulto', 'idoso'])
df['risco_combinado'] = df['hypertension'] + df['heart_disease'] + (df['avg_glucose_level'] / df['avg_glucose_level'].max())

print("\nMédia das variáveis por status de AVC (stroke):")
print(df.groupby('stroke')[['age', 'avg_glucose_level', 'bmi', 'risco_combinado']].mean().round(2))

sns.histplot(data=df, x='age', hue='stroke', kde=True)
plt.title('Distribuição de Idade por Ocorrência de AVC')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.legend(title='AVC')
plt.savefig('imagens/grafico_idade_avc.png', dpi=300)
plt.show()

sns.boxplot(x='stroke', y='avg_glucose_level', data=df)
plt.title('Boxplot de Glicemia por Status de AVC')
plt.xlabel('Status de AVC')
plt.ylabel('Glicemia Média')
plt.savefig('imagens/boxplot_glicemia.png', dpi=300)
plt.show()

jovens_saudaveis = df[(df['faixa_etaria'] == 'jovem') &
                      (df['hypertension'] == 0) &
                      (df['heart_disease'] == 0)]

print("\nCasos de AVC entre jovens sem comorbidades:")
print(jovens_saudaveis['stroke'].value_counts())
print(f"Total de jovens sem comorbidades: {len(jovens_saudaveis)}")

sns.scatterplot(data=jovens_saudaveis, x='avg_glucose_level', y='bmi', hue='stroke')
plt.title('Jovens sem Comorbidades - Glicemia vs IMC')
plt.xlabel('Glicemia')
plt.ylabel('IMC')
plt.legend(title='AVC')
plt.savefig('imagens/dispersao_jovens_saudaveis.png', dpi=300)
plt.show()

corr = df.drop(columns=['id', 'faixa_etaria']).corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.3,
    linecolor='white',
    square=True,
    cbar=False,
    annot_kws={"size": 8}
)
plt.title('Matriz de Correlação entre Variáveis Numéricas', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(rotation=0, fontsize=9)
plt.tight_layout()
plt.savefig('imagens/heatmap_correlacao.png', dpi=300)
plt.show()

z_scores = stats.zscore(df[['avg_glucose_level', 'bmi']])
outliers = (np.abs(z_scores) > 3).any(axis=1)
print("\nTotal de outliers detectados (Z-score > 3) em glicemia ou IMC:")
print(outliers.sum())

sns.boxplot(data=df[['avg_glucose_level', 'bmi']])
plt.title('Boxplots - Glicemia e IMC')
plt.ylabel('Valor')
plt.xticks([0, 1], ['Glicemia', 'IMC'])
plt.savefig('imagens/boxplot_glicemia_bmi.png', dpi=300)
plt.show()

sns.histplot(data=df, x='avg_glucose_level', hue='stroke', kde=True)
plt.title('Distribuição de Glicemia por Status de AVC')
plt.xlabel('Glicemia')
plt.ylabel('Frequência')
plt.legend(title='AVC')
plt.savefig('imagens/histograma_glicemia.png', dpi=300)
plt.show()

scaler = StandardScaler()
cluster_data = scaler.fit_transform(df[['age', 'avg_glucose_level', 'bmi']])

sse = []
for k in range(1, 10):
    km = KMeans(n_clusters=k, random_state=0)
    km.fit(cluster_data)
    sse.append(km.inertia_)

print("\nSSE por valor de k (Elbow Method):")
for i, val in enumerate(sse, start=1):
    print(f"k={i}: SSE={val:.2f}")

plt.plot(range(1, 10), sse, marker='o')
plt.title('Elbow Method para Definição do Número de Clusters')
plt.xlabel('Número de Clusters')
plt.ylabel('Soma dos Erros Quadráticos Internos (SSE)')
plt.savefig('imagens/elbow_method.png', dpi=300)
plt.show()

km = KMeans(n_clusters=3, random_state=0)
df['cluster'] = km.fit_predict(cluster_data)

print("\nTotal de pacientes por cluster:")
print(df['cluster'].value_counts().sort_index())

print("\nPorcentagem de pacientes com AVC por cluster:")
cluster_avc = df.groupby('cluster')['stroke'].mean().round(3) * 100
print(cluster_avc.to_frame(name='% AVC por Cluster'))

sns.scatterplot(x='age', y='avg_glucose_level', hue='cluster', data=df, palette='Set1')
plt.title('Agrupamento de Pacientes por Idade e Glicemia')
plt.xlabel('Idade')
plt.ylabel('Glicemia')
plt.legend(title='Cluster')
plt.savefig('imagens/dispersao_clusters.png', dpi=300)
plt.show()