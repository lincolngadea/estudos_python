import pandas as pd

df = pd.DataFrame({
    'Idade': ['30', '25', '28', '35', '40'],
    'Salario': ['1000', '1250', '2500', '2840', '5800']
})

print(df.describe())
print()
print(df.info())
print()

# Alterando o tipo de dado na coluna
df['Idade'] = df['Idade'].astype('int32')
df['Salario'] = df['Salario'].astype('float')

print(df.info())
print(df.describe())
print()

# Usando o Metodo toNumeric para alterar o tipo de dado
df = pd.DataFrame({'idade': ['25', '30', '40', '35']})
df['idade'] = pd.to_numeric(df['idade'])
print(df.describe())
print(df.info())
print(df.dtypes)
print()

# Metodo para transformar no tipo data toDatetime
df = pd.DataFrame({'Data': ['25/05/2023', '30/06/2023', '15/09/2023']})
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
print(df.dtypes)
print(df)
print()

# Como calcular datas
dados = {'Atividade': ['A', 'B', 'C'],
         'Inicio_Atividade': ['2023-05-01 09:00:00', '2023-05-02 14:30:00', '2023-05-03 10:15:00'],
         'Termino_Atividade': ['2023-05-01 11:30:00', '2023-05-03 16:45:00', '2023-05-03 10:15:00']}

df = pd.DataFrame(dados)

df['Inicio_Atividade'] = pd.to_datetime(df['Inicio_Atividade'])
df['Termino_Atividade'] = pd.to_datetime(df['Termino_Atividade'])

df['Duracao_Atividade'] = df['Termino_Atividade'] - df['Inicio_Atividade']
print(df)
