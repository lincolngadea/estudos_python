"""
Qual é o estado com a maior média de salário entre os clientes?
"""
import pandas as pd

# carrega os dados
dados_cli = pd.read_csv('./dados/clientes_informacoes_demograficas.csv', sep=';')

df_cli = pd.DataFrame(dados_cli)

estado_salario_cli = df_cli[['Estado','Salário']]

# Identifica a média salarial por estado
media_salarial_por_estado = estado_salario_cli.groupby('Estado')['Salário'].mean()
# print(f"Média Salarial por estado:{media_salarial_por_estado}")

# Estado com maior salário
estado_maior_salario = media_salarial_por_estado.idxmax()
maior_media_salario = media_salarial_por_estado.max()

print(f"O Estado de {estado_maior_salario} possui a maior média salarial com R${maior_media_salario:.2f}")