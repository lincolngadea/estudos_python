import pandas as pd

dados = {'Nome': ['Maria', 'Joao', 'Ana'],
         'Idade': [20, 19, 30]}

df = pd.DataFrame(dados)

# Usando o metodo assign para criar novas colunas baseadas nos valores especificos
# O Processo acontece com uso de lambdas

df = df.assign(Ano_Nascimento=lambda x: 2024 - x['Idade'])
# print(df)

# Metodo Transform
# Usado para aplicar uma operacao em um determinado grupo de linhas com base em uma coluna

dados = {'Grupo': ['A', 'B', 'A', 'B'],
         'Valor': [10, 20, 30, 40]}

df = pd.DataFrame(dados)

# Aplicar uma operação de média por grupo usando transform
df['Media_Grupo'] = df.groupby('Grupo')['Valor'].transform('mean')

# Metodo Apply
# Aplica uma funcao para cada linha ou coluna do Dataframe

dados = {'Valor1': [10, 20, 30],
         'Valor2': [5, 10, 15]}
df = pd.DataFrame(dados)

df['Resultado'] = df.apply(lambda row: row['Valor1'] * row['Valor2'], axis=1)

#Usando apply com funções

def verifica_resultado(Resultado):
    if Resultado >= 200:
        return 'Vendas dentro da meta'
    else:
        return 'Vendas abaixo da meta'

df['Avaliacao_Vendas'] = df['Resultado'].apply(verifica_resultado)

print(df)
