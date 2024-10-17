import numpy as np
import pandas as pd

# CRIANDO UM DATA FRAME A PARTIR DE UMA LISTA

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

# print(controle_vendas)
df = pd.DataFrame(list_vendas, columns=['Cliente', 'Produto', 'Quant', 'Vlr Unit'])
print(df)
