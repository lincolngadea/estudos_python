"""
Crie um boxplot dos salários de todas as pessoas que
possuem escolaridade superior. Em seguida, escolha
a melhor representação gráfica.
"""
import pandas as pd
import matplotlib.pyplot as plt

from avaliacao_02.q4 import df_cli

dados_cli = pd.read_csv('./dados/clientes_informacoes_demograficas.csv', sep=';')

df_cli = pd.DataFrame(dados_cli)

nivel_superior = df_cli[df_cli['Escolaridade'] == 'Superior']
# print(df_cli[nivel_superior])

nivel_superior['Salário'].plot(
    kind='box',
    vert=False,
    patch_artist=True,
    widths=0.5
)

# plt.boxplot(nivel_superior['Salário'], patch_artist=True)

plt.title('Boxplot dos Salários - Nível Superior')
plt.xlabel('Salário')
plt.ylabel('Escolaridade')

plt.show()
