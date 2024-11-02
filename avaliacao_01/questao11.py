import pandas as pd
import numpy as np

# Configuração para exibir todas as colunas
# pd.set_option('display.max_columns', None)

# Carregar os dados
fin_data1 = pd.read_csv('vendas_produtos_financeiros.csv', sep=';', encoding='latin1')
fin_data2 = pd.read_csv('dados_vendas_produtos.csv', sep=';', encoding='latin1')
df1 = pd.DataFrame(fin_data1)
df2 = pd.DataFrame(fin_data2)

# Lista de estados do Nordeste
estados_nordeste = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]

# Filtrar os dados para os estados do Nordeste
vendas_filtradas = df1.query('Estado in @estados_nordeste')

# Calcular o valor total de vendas
# vendas_filtradas.loc[:, 'Valor_Total'] = vendas_filtradas['Quantidade'] * vendas_filtradas['Preco_Unitario']

# Exibir as vendas filtradas
print(vendas_filtradas)
print()

# Somar o valor total das vendas
total_vendas = vendas_filtradas['Valor_Total'].mean()
print(total_vendas)