import pandas as pd
import numpy as np

fin_data = pd.read_csv('vendas_produtos_financeiros.csv', sep=';', encoding='latin1')
df = pd.DataFrame(fin_data)
df_sem_nulos = df.dropna()

df_sem_duplicatas = df_sem_nulos.drop_duplicates()

df_filtrado = df.query('Estado == "SP"')

media = df_filtrado['Valor_Total'].mean()
print(media)
