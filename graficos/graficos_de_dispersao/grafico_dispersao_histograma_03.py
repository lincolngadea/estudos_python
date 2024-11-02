import pandas as pd
import matplotlib.pyplot as plt

dados = [10, 15, 20, 22, 25, 28, 30, 32, 35, 38, 40, 42, 45, 50, 55, 60, 65, 70]

df = pd.DataFrame(dados, columns=['Valores'])

# Criando um histograma com uma personalização nos intervalos

intervalos = [0,20,40,60,80]
bins = len(intervalos) -1

# Criando o histograma
plt.hist(
    df['Valores'],
    bins = bins,
    edgecolor = 'black'
)

# Personalizando o histograma
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma Personalizado')

# configurando os intervalos no eixo X
plt.xticks(intervalos)

# Exibindo o gráfico
plt.show()

