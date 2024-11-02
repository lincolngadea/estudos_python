import numpy as np
import pandas as pd
import os

fin_data = pd.read_csv('vendas_produtos_financeiros.csv', sep=';', encoding='latin1')
df = pd.DataFrame(fin_data)

# print(df.isna().sum()) #quantidade de dados auxentes

df_completo = df.dropna()
# print(df_completo)

df_duplicado = df_completo.duplicated(keep='first')
df_duplicado_view = df_completo[df_duplicado]

print(df_duplicado_view.sum())

# print(df_duplicado_view)

df_unico = df_completo.drop_duplicates()

# print(df_unico)