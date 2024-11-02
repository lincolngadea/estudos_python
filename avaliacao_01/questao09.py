import pandas as pd
import numpy as np

# Configuração para exibir todas as colunas
# pd.set_option('display.max_columns', None)

# Carregar os dados
fin_data = pd.read_csv('vendas_produtos_financeiros.csv', sep=';', encoding='latin1')
df = pd.DataFrame(fin_data)

vendas_filtradas= df.query('Produto == "Produto 8" and Estado == "PE"')

print(vendas_filtradas)
print()

media_de_vendas = vendas_filtradas['Quantidade'].mean()
print(media_de_vendas)