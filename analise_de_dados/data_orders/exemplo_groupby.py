import pandas as pd

dados = {'Nome': ['Lincoln', 'Pedro', 'Rafael', 'Christiny', 'Melissa'],
         'Categoria': ['A', 'B', 'A', 'B', 'B'],
         'Vendas': [230.0, 350.0, 300.0, 180.0, 200.0]
         }

df = pd.DataFrame(dados)

#Agrupamento de dados com soma
df_agrupado1= df.groupby('Categoria')['Vendas'].sum()
df_agrupado2 = df.groupby('Nome')['Vendas'].sum()

#Agrupra várias funções em um único agrupamento

#Forma inline
df_agrupado3 = df.groupby('Categoria').agg({'Vendas':['sum','mean','max']})

#Forma inblok
df_agrupado4 = df.groupby('Categoria')
df_agrupamento = df_agrupado4.agg(
    Total_vendas = ('Vendas','sum'),
    Media_vendas = ('Vendas','mean'),
    Maior_venda = ('Vendas', 'max')
)

#Usando o metodo pivot_table
#Permite criar uma tabela dinâmica a partir dos dados,
# onde as linhas representam uma categoria,
# as colunas representam outra categoria e os valores
# são agregados com base em uma terceira categoria.

# Criar uma tabela dinâmica com base nas colunas 'Categoria' e 'Nome'
df_pivot = df.pivot_table(index='Categoria', columns='Nome', values='Vendas', aggfunc='sum')
# print(df_pivot)

#Permite criar uma tabela de frequência cruzada,
# que mostra a contagem dos valores em duas ou mais colunas.

# Criar uma tabela de frequência cruzada com base nas colunas 'Categoria' e 'Nome'
venda_cross = pd.crosstab(df['Categoria'], df['Nome'])

# print(venda_cross)

#Metodo info
# Fornece um resumo conciso das informações básicas sobre um DataFrame,

df_info = df.info()
# print(df_info)

#metodo describe
#Fornece um resumo estatístico das colunas numéricas de um DataFrame.

df_describe = df.describe()
# print(df_describe)

#metodo transpose
#Transforma linha em coluna e coluna em linha

print(df.transpose())
print(df.describe().transpose())
