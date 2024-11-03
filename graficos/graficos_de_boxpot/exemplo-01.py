import matplotlib.pyplot as plt
import numpy as np

dados1 = np.random.normal(0, 1, 100)
dados2 = np.random.normal(0, 2, 100)
dados3 = np.random.normal(0, 3, 100)

# Lista de dados
dados = [dados1, dados2, dados3]

# Gráfico de boxplot
plt.boxplot(dados)

# Rótulos e títulos
plt.xticks([1, 2, 3], ['Dados 1', 'Dados 2', 'Dados 3'])
plt.xlabel('Variáveis')
plt.ylabel('Valores')
plt.title('Gráfico de Boxplot')

# Exibição do gráfico
plt.show()
