import numpy as np
import pandas as pd

dados = [
    ["Ana", "Camiseta", 3, 29.90],
    ["Bruno", "Calça", 2, 99.90],
    ["Carla", "Sapato", 1, 149.90],
    ["Diego", "Boné", 5, 19.90],
    ["Elaine", "Bolsa", 2, 79.90],
    ["Fabio", "Relógio", 1, 199.90],
    ["Gustavo", "Óculos", 4, 59.90],
    ["Helena", "Carteira", 3, 39.90],
    ["Isabela", "Jaqueta", 1, 299.90],
    ["João", "Tênis", 2, 249.9]
]

df = pd.DataFrame(dados, columns=('Cliente','Produto','Quant','Preço'))
print(df)

print('__________________________________')
result = df.query('Quant > 3 and Cliente == "Diego"')
print(result)

print('__________________________________')
result = df.query('Quant in (3,4)')
print(result)