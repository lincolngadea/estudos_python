"""
Qual é a distribuição da idade dos clientes? Utilize bins=30
"""
import pandas as pd
import matplotlib.pyplot as plt

# carrega os dados
dados_cli = pd.read_csv('./dados/clientes_informacoes_demograficas.csv', sep=';')

df_cli = pd.DataFrame(dados_cli)

idade_cli = df_cli['Idade']

plt.hist(
    idade_cli,
    bins=30,
    edgecolor='black'
)

plt.xlabel('Idades')
plt.ylabel('Frequencia')
plt.title('Gráfico de idades')

plt.show()