import pandas as pd

# Criando o dicionário de dados
dados = {
    'nome': ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Carla', 'Paulo', 'Fernanda', 'Ricardo', 'Juliana',
             'Marcos', 'Beatriz', 'Rafael', 'Camila', 'Bruno', 'Larissa', 'Gustavo', 'Patrícia', 'Felipe', 'Sofia'],
    'idade': [25, 30, 22, 28, 35, 27, 40, 32, 29, 26, 33, 31, 24, 23, 36, 34, 38, 37, 21, 20],
    'salario': [2500, 3200, 2200, 2800, 3500, 2700, 4000, 3200, 2900, 2600,
                3300, 3100, 2400, 2300, 3600, 3400, 3800, 3700, 2100, 2000]
}

# Gerando o DataFrame
df = pd.DataFrame(dados)

#Ordenando dados com Sort Values
df_sort = df.sort_values('idade')
df_sort_desc = df.sort_values('idade', ascending=False)

#Ordenando pelo índice
df_sort_index = df.sort_index() #Ordena do menor para o maior índice
df_sort_index_desc = df.sort_index(ascending=False) #Ordena do maior para o menor índice

# Exibindo o DataFrame
# print(df_sort_index_desc)

#Criando uma Série
serie_data = pd.Series([10,20,30,40], index=['d','b','c','a'])

#Ordenando a série pelo index
serie_sort_index = serie_data.sort_index() #padrão ascendente
serie_sort_index_desc = serie_data.sort_index(ascending=False) #Padrão descendente


#Exibindo a série
print(serie_sort_index_desc)

