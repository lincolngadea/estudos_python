import pandas as pd
import numpy as np

# Configuração para exibir todas as colunas
pd.set_option('display.max_columns', None)

# Carregar os dados
fin_data = pd.read_csv('vendas_produtos_financeiros.csv', sep=';', encoding='latin1')
df = pd.DataFrame(fin_data)

# Remover nulos e duplicatas
df_sem_nulos = df.dropna()
df_sem_duplicatas = df_sem_nulos.drop_duplicates()

# total = df_sem_duplicatas.groupby('Produto')['Quantidade'].max()

# Exibir o DataFrame completo
soma_quantidades = df.groupby('Produto')['Quantidade'].sum()
produto_mais_vendido = soma_quantidades.idxmax()
quantidade_total_maxima = soma_quantidades.max()
print(produto_mais_vendido)
print(quantidade_total_maxima)
print(soma_quantidades)