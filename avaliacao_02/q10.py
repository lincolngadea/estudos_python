"""
Qual é a média de idade das pessoas
com mais de três cartões de crédito?
"""
import pandas as pd

dados_caract_cli = pd.read_csv('./dados/clientes_caracteristicas_fisicas.csv', sep=',')
dados_demog_cli = pd.read_csv('./dados/clientes_informacoes_demograficas.csv', sep=';')

df_caract_cli = pd.DataFrame(dados_caract_cli)
df_demog_cli = pd.DataFrame(dados_demog_cli)

df_cli = pd.merge(df_demog_cli,df_caract_cli, on='ID Cliente')
print(df_cli['Número de Cartões de Crédito'])
cartao = (df_cli['Número de Cartões de Crédito'] >= 3)
print(cartao)
media_idade = df_cli.loc[cartao, 'Idade'].mean()
print(media_idade)