import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np

df = pd.read_csv('dados_clinicos2.csv', sep=';')

df.describe()

x_peso = df.iloc[:,1].values
x_peso

y_colesterol = df.iloc[:,2].values
y_colesterol

correlacao = df.corr()
plot = sns.heatmap(correlacao, annot = True, linewidths=.3)
plot

from sklearn.linear_model import LinearRegression
previsao_reta = LinearRegression()

type(previsao_reta)

X_peso = x_peso.reshape(-1,1)

previsao_reta.fit(X_peso, y_colesterol)

