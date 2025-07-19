from scipy import stats
import pandas as pd

def detectar_outliers(df):
    z_scores = stats.zscore(df[['avg_glucose_level', 'bmi']])
    outliers = (abs(z_scores) > 3).any(axis=1)
    print("\nTotal de outliers detectados (Z-score > 3):")
    print(outliers.sum())