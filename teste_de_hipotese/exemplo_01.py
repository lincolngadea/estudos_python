import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns

# Carregando a base de dados
df = pd.read_csv('tempo_medio_tarefas.csv')

# Criando uma figura com as duas subplots lado a lado
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(8,3))

# Plotagem do histograma do grupo A
sns.histplot(df['grupo_a'],ax=ax1, kde=True, color='blue')
ax1.set_xlabel('Grupo A')
ax1.set_title('Distribuição do Grupo A')

# Plotagem do histograma do grupo B
sns.histplot(df['grupo_b'],ax=ax2, kde=True, color='red')
ax2.set_xlabel('Grupo B')
ax2.set_title('Distribuição do Grupo B')

# Ajuste no layout
plt.tight_layout()

# Aplicando o teste T student
t_statistic, p_value = stats.ttest_ind(df['grupo_a'],df['grupo_b'])
print(f'Estatística t:{t_statistic}')
print(f'Valor-p:{p_value}')

# Plotagem
# plt.show()