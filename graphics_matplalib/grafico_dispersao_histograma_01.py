import pandas as pd
import matplotlib.pyplot as plt

dados = [10, 15, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 50, 55, 60, 65, 70]

df = pd.DataFrame(dados, columns=['Valores'])

plt.hist(
    df['Valores'],
    bins=5,
    edgecolor='black'
)

plt.xlabel('Valores')
plt.ylabel('Frequencias')
plt.title('Gráfico de histograma')

plt.show()