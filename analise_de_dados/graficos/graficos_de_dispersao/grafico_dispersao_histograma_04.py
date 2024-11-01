import matplotlib.pyplot as plt
import numpy as np

# Gera dados aleatórios
dados1 = np.random.normal(50,10,1000)
dados2 = np.random.normal(70,5,1000)

# Criando o histograma empilhado

plt.hist(
    [dados1,dados2],
    bins=20,
    color=['red','green'],
    label=['Dist 01','Dist 02'],
    edgecolor='black',
    stacked=True
)

# Personalizando o histograma
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma Empilhado')
plt.legend()

# Exibindo o gráfico
plt.show()