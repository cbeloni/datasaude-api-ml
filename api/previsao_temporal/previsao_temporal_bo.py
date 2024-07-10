import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import statsmodels.api as sm
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt
import joblib

def load_df(arquivo: str):
    df = pd.read_csv(arquivo, sep='|')
    return df

df = load_df('dados_treino_statsmodel_2022.csv')
# df.to_csv('temp_file.csv', sep='|', index=False, mode='a', header=True)
df.head()