import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

#Dados de horas de estudo e notas de alunos

dados = {
    'horas_estudo': [5,7,3,4,6],
    'notas':[80,85,70,75,90]
}

df = pd.DataFrame(dados)

# Correlação de pearson

coef_corr, p_value = stats.pearsonr(df['horas_estudo'], df['notas'])
print(f'Coeficiente de correlação: {coef_corr}')
print(f'Valor P: {p_value}')