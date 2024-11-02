import matplotlib.pyplot as plt
import pandas as pd

categorias = ['A','B','C','D']
valores = [30,25,20,15]

# Criando um gráfico de pizza
plt.pie(valores, labels=categorias)

# Exibição do gráfico
plt.show()