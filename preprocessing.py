import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def preparar_dados(df):
    df['bmi'] = df['bmi'].fillna(df['bmi'].median())
    df['smoking_status'] = df['smoking_status'].replace('Unknown', np.nan)
    df['smoking_status'] = df['smoking_status'].fillna('never smoked')
    df.drop_duplicates(inplace=True)

    le = LabelEncoder()
    for col in ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']:
        df[col] = le.fit_transform(df[col])

    df['faixa_etaria'] = pd.cut(df['age'], bins=[0, 30, 60, 100], labels=['jovem', 'adulto', 'idoso'])
    df['risco_combinado'] = df['hypertension'] + df['heart_disease'] + (df['avg_glucose_level'] / df['avg_glucose_level'].max())
    return df