import pandas as pd

dados_pessoa = {
    'ID': [1, 2, 3, 4],
    'Nome': ['Lincoln', 'Pedro', 'Rafael', 'Chris'],
    'Idade': [25, 19, 17, 35]
}

dados_profissao = {
    'ID': [1, 2, 5, 6],
    'Profissao': ['Engenheiro', 'Medico', 'Advogado', 'Professor']
}

df1 = pd.DataFrame(dados_pessoa)
df2 = pd.DataFrame(dados_profissao)

# Reune os dados com Ids correspondentes entre dois ou mais DataFrames

print('Usando o MERGE COM INNER JOIN')
df_inner = pd.merge(df1,df2, on='ID', how='inner')
print(df_inner)
print()

# Reune todos os dados entre dois frames
# e seta como NaN os que não possuem IDs correspondentes

print('Usando o MERGE COM OUTER JOIN')
df_outer = pd.merge(df1,df2, on='ID', how='outer')
print(df_outer)
print()

# Reune todos os dados entre dois frames
# e seta como NaN os que não possuem IDs correspondentes no DataFrame a DIREITA

print('Usando o MERGE LEFT JOIN')
df_left = pd.merge(df1,df2, on='ID', how='left')
print(df_left)
print()

# Reune todos os dados entre dois frames
# e seta como NaN os que não possuem IDs correspondentes no DataFrame a ESQUERDA

print('Usando o MERGE COM RIGHT JOIN')
df_right = pd.merge(df1,df2, on='ID', how='right')
print(df_right)

# METODO JOIN COM INNER
# Funciona como o Merge, só que utilizando ÍNDICES

df_join_inner = df1.set_index('ID').join(df2.set_index('ID'), how='inner')
print(f'Resultado inner join:\n{df_join_inner}')
print()

# METODO JOIN OUTER
# Funciona como o Merge, só que utilizando ÍNDICES

df_join_outer = df1.set_index('ID').join(df2.set_index('ID'), how='outer')
print(f'Resultado outer join:\n{df_join_outer}')
print()

# METODO JOIN LEFT
# Funciona como o Merge, só que utilizando ÍNDICES

df_join_left = df1.set_index('ID').join(df2.set_index('ID'), how='left')
print(f'Resultado outer join:\n{df_join_left}')
print()

# METODO JOIN RIGHT
# Funciona como o Merge, só que utilizando ÍNDICES

df_join_right = df1.set_index('ID').join(df2.set_index('ID'), how='right')
print(f'Resultado outer join:\n{df_join_right}')
print()

# METODO CONCAT
# Permite combinar Data frames ao longo de seus eixos
# Concatenando eixos horizontais
df3 = pd.DataFrame({'Nova_idade':[25,20,18]})

df_concat_horizontal = pd.concat([df1,df3],axis=1)
print(df_concat_horizontal)
print()

# Concatenando eixo vertical
df_concat_vertical = pd.concat([df1,df2])
print(df_concat_vertical)

