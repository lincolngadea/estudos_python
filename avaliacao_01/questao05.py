import pandas as pd
import numpy as np

fin_data = pd.read_csv('vendas_produtos_financeiros.csv', sep=';')
df = pd.DataFrame(fin_data)
df_sem_nulos = df.dropna()

df_sem_duplicatas = df_sem_nulos.drop_duplicates()

df_filtrado = df_sem_duplicatas.query('Estado == "PE"')

print(df_filtrado.head())

desvio_padrao = df_filtrado['Preco_Unitario'].std()
print(desvio_padrao)
