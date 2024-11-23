"""
Existe alguma correlação entre a altura e o peso dos clientes?
"""

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega dados
dados_cli = pd.read_csv('./dados/clientes_caracteristicas_fisicas.csv', sep=',')

df_dados_cli = pd.DataFrame(dados_cli)

# Correlacionando

coef_corr, p_value = stats.pearsonr(df_dados_cli['Altura (cm)'], df_dados_cli['Peso (kg)'])

print(f'Coeficiente de correlação: {coef_corr}')

print(f'Valor P: {p_value}')

# Visualização
plt.figure(figsize=(8, 6))
sns.regplot(
    x='Altura (cm)',
    y='Peso (kg)',
    data=df_dados_cli,
    scatter_kws={'alpha': 0.6},
    line_kws={'color': 'red'}
)
plt.title('Correlação entre Altura e Peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.grid(True)
plt.show()
