import pandas as pd
import matplotlib.pyplot as plt

# Vamos imaginar que estamos realizando uma análise de um grupo de pessoas,
# coletando informações sobre altura, peso e idade. Nosso objetivo é investigar
# se existe alguma relação entre essas variáveis e entender melhor como elas se relacionam entre si.

# Para isso, coletamos dados de 10 indivíduos e armazenamos em um DataFrame.
# Cada linha do DataFrame representa uma pessoa, e as colunas representam as variáveis:
# altura, peso e idade.

# Através do gráfico de dispersão, podemos visualizar a relação entre altura e peso.
# Cada ponto no gráfico representa uma pessoa do grupo, onde o eixo x representa a
# altura em centímetros e o eixo y representa o peso em quilogramas.

dados = {
    'altura': [165, 170, 175, 168, 172, 180, 160, 155, 162, 175],
    'peso': [60, 65, 70, 63, 68, 75, 55, 50, 58, 70],
    'idade': [25, 30, 35, 28, 32, 40, 22, 20, 24, 34]
}

df = pd.DataFrame(dados)

plt.scatter(
    df['altura'],
    df['peso'],
    c=df['idade'],
    marker='o',
    s=80,
    alpha=0.8
)

plt.xlabel('Altura(cm)')
plt.ylabel('Peso(Kg)')
cbar = plt.colorbar()
cbar.set_label('Idade')

plt.show()
