"""
Qual é a média de altura para as pessoas que residem no estado de MG,
são solteiras e possuem filhos?
"""
import pandas as pd

dados_caract_cli = pd.read_csv('./dados/clientes_caracteristicas_fisicas.csv', sep=',')
dados_demog_cli = pd.read_csv('./dados/clientes_informacoes_demograficas.csv', sep=';')

df_caract_cli = pd.DataFrame(dados_caract_cli)
df_demog_cli = pd.DataFrame(dados_demog_cli)

df_cli = pd.merge(df_demog_cli,df_caract_cli, on='ID Cliente')
# print(df_cli['Estado Civil'])

dados_tratados = (df_cli['Estado'] == 'MG') & (df_cli['Estado Civil'] == 'Solteiro') & (df_cli['Tem Filhos'] == 'Sim')

media_altura = df_cli.loc[dados_tratados, 'Altura (cm)'].mean()

print(media_altura)