"""
Qual é a quantidade de pessoas
que possuem tipo de sangue O+ e que possuem filhos?
"""
import pandas as pd

dados_caract_cli = pd.read_csv('./dados/clientes_caracteristicas_fisicas.csv', sep=',')
dados_demog_cli = pd.read_csv('./dados/clientes_informacoes_demograficas.csv', sep=';')

df_caract_cli = pd.DataFrame(dados_caract_cli)
df_demog_cli = pd.DataFrame(dados_demog_cli)

df_inner = pd.merge(df_caract_cli, df_demog_cli, on='ID Cliente')

#transforma tudo em minúsculo
df_inner['Tem Filhos'] = df_inner['Tem Filhos'].str.lower()

tipo_sang = (df_inner['Tipo Sanguíneo'] == 'O+') & (df_inner['Tem Filhos'] == 'sim')
resultado = tipo_sang.sum()

print(f"Quantidade de clientes com tipo sanguíneo O+ e que possuem filhos: {resultado}")
