from scipy import stats
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dados de preferência de comida e sexo
preferencias = ["Pizza", "Hambúrguer", "Pizza", "Salada", "Hambúrguer"]
sexo = ["Masculino", "Feminino", "Masculino", "Feminino", "Masculino"]

# Tabela de contigência
tabela_contigencia = pd.crosstab(preferencias,sexo)
print(tabela_contigencia)

# Teste de qui quadrado
result = stats.chi2_contingency(tabela_contigencia)

# Visão dos resultados
print(f'\n Estatísticas de chi-quadrado: {result.statistic}')
print(f'\n Valor P: {result.pvalue}')

# Gráfico de barras empilhados
sns.set_theme(style='darkgrid')
ax = tabela_contigencia.plot(kind='bar', stacked=True)

# Configurar os rótulos e títulos
ax.set_xlabel('Preferências de Comida')
ax.set_ylabel('Contagem')
ax.set_title('Preferências de comida por gênero')

# Plota o gráfico
plt.tight_layout()
plt.show()