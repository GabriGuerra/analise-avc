import pandas as pd
import os

if not os.path.exists('healthcare-dataset-stroke-data.csv'):
    raise FileNotFoundError("Arquivo de dados não encontrado. Baixe o dataset do Kaggle e salve como 'healthcare-dataset-stroke-data.csv'")

def carregar_dados():
    df = pd.read_csv('healthcare-dataset-stroke-data.csv')
    print("\nInformações do DataFrame:")
    print(df.info())
    print("\nEstatísticas descritivas:")
    print(df.describe())
    return df