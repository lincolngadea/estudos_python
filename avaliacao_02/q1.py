"""
Após a coleta de todos os dados, responda:
quantos códigos de hobbies distintos estão presentes na base de dados?
"""
import pandas as pd

# Carregar os dados
dados_demog = pd.read_csv('./dados/clientes_informacoes_demograficas.csv', sep=';')

# Criar DataFrames
df_dados_demog = pd.DataFrame(dados_demog)

col_hobby_demog = df_dados_demog['Hobbies (Código)']
col_hobby_demog = col_hobby_demog.str.strip().str.lower()
demog_unicos = col_hobby_demog.unique()
quant_demog_unicos = len(demog_unicos)

print("Quantidade de hobbies demog:",quant_demog_unicos)

