import pandas as pd

fin_data = pd.read_csv('vendas_produtos_financeiros.csv', sep=';', encoding='latin1')
df = pd.DataFrame(fin_data)
df_completo = df.dropna()

df_duplicado = df_completo.duplicated(keep=False)
df_duplicado_view = df_completo[df_duplicado]

df_duplicados_unicos = df_duplicado_view.drop_duplicates()

quant_duplicados_unicos = df_duplicados_unicos.shape[0]

print(quant_duplicados_unicos)
