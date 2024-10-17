import pandas as pd
import numpy as np

list_vendas = [
    ['Lincoln', 'Melancia', np.random.randint(1, 10), np.around(np.random.uniform(10.0, 100.0))],
    ['Rafael', 'Morango', np.random.randint(1, 10), np.around(np.random.uniform(10.0, 100.0))],
    ['Pedro', 'Banana', np.random.randint(1, 10), np.around(np.random.uniform(10.0, 100.0))],
    ['Chris', 'Maracujá', np.random.randint(1, 10), np.around(np.random.uniform(10.0, 100.0))],
    ['Jackson', 'Coco', np.random.randint(1, 10), np.around(np.random.uniform(10.0, 100.0))],
    ['Graça', 'Laranja', np.random.randint(1, 10), np.around(np.random.uniform(10.0, 100.0))],
    ['Kelly', 'Manga', np.random.randint(1, 10), np.around(np.random.uniform(10.0, 100.0))],
    ['Itamar', 'Uva', np.random.randint(1, 10), np.around(np.random.uniform(10.0, 100.0))],
    ['Neto', 'Pera', np.random.randint(1, 10), np.around(np.random.uniform(10.0, 100.0))],
    ['Andrezza', 'Amora', np.random.randint(1, 10), np.around(np.random.uniform(10.0, 100.0))]
]

df = pd.DataFrame(list_vendas, columns=('Cliente','Produto','Quant','Preço'))
print(df)

print('__________________________________')
#Seleciona colunas específicas
df_col = df.loc[:, ['Cliente', 'Produto', 'Quant']]
print(df_col)

print('----------------------------------')
#Seleciona as linhas de colunas específicas
df_line = df.loc[[2,3],:]
print(df_line)

print('----------------------------------')
#Seleciona linhas e colunas específicas
df_espec = df.loc[df['Cliente']=='Lincoln']
print(df_espec)

print('----------------------------------')
#Seleciona Linhas e colunas usando os índices
df_line_col = df.iloc[[1,3],[0,1]]
print(df_line_col)

print('----------------------------------')
#Usando o at para selecionar o índice de uma linha e uma coluna específica
df_line_col_esp = df.at[3,'Cliente']
print(df_line_col_esp)

print('----------------------------------')
#Usando o head para selecionar os primeiros elementos da lista
df_head = df.head(3)
print(df_head)

print('----------------------------------')
#Usando o tail para selecionar os últimos elementos da lista
df_tail = df.tail(3)
print(df_tail)

print('----------------------------------')
#Usando o sample para exibição de uma amostra dos dados
df_sample = df.sample(4)
print(df_sample)
