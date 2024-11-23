"""
Qual é o estado com a maior proporção de salários acima
de 5000 reais entre os clientes?
"""
import pandas as pd

dados_cli = pd.read_csv('./dados/clientes_informacoes_demograficas.csv', sep=';')

df_cli = pd.DataFrame(dados_cli)

df_cli['Salario_Acima_5000'] = df_cli['Salário'] > 5000

proporcao = df_cli.groupby('Estado')['Salario_Acima_5000'].mean()

estado_maior_proporcao = proporcao.idxmax()
maior_proporcao = proporcao.max()

print(f"Estado com maior proporção de salários acima de 5000: {estado_maior_proporcao}")
print(f"Proporção: {maior_proporcao:.2f}")
