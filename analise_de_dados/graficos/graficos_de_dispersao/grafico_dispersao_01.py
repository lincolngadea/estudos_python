import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

# Criação do gráfico de dispersão

plt.scatter(x,y)
plt.xlabel('Variável X')
plt.ylabel('Variável Y')
plt.title('Gráfico de dispersão')
plt.legend()
plt.show()
