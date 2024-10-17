import pandas as pd
import numpy as np

dados = [
    ["Ana", 28, "Feminino", "Camiseta", 3, 29.90],
    ["Bruno", np.nan, "Masculino", "Calça", 2, 99.90],
    ["Carla", 32, np.nan, "Sapato", 1, 149.90],
    ["Diego", 24, "Masculino", np.nan, 5, 19.90],
    ["Elaine", np.nan, "Feminino", "Bolsa", np.nan, 79.90],
    ["Fabio", 45, "Masculino", "Relógio", 1, np.nan],
    ["Gustavo", 29, np.nan, "Óculos", 4, 59.90],
    ["Helena", np.nan, "Feminino", "Carteira", 3, 39.90],
    [np.nan, 37, "Feminino", "Jaqueta", 1, 299.90],
    ["João", 40, np.nan, "Tênis", np.nan, 249.90]
]

df = pd.DataFrame(dados, columns=('Nome','Idade','Gênero','Produto','Quantidade','Preço'))
print(df)

# Metodo ISNA -É utilizada para identificar valores faltantes
# em um dataframe. Ela retorna uma matriz booleana do mesmo tamanho
# do dataframe, em que cada elemento é True se o valor correspondente
# no dataframe for nulo (NaN) e False caso contrário.
print('____________________________________________')
print(df.isna()) #Retorna true nos campos onde os valores estão auxentes
print(df.isna().sum()) # Retorna a quantidade de valores auxentes em cada coluna
