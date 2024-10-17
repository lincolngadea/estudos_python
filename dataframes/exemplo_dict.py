import numpy as np
import pandas as pd

# CRIANDO UM DATA FRAME A PARTIR DE UM DICIONÁRIO

dict_vendas = {
    'Cliente': ['Lincoln', 'Rafael', 'Pedro', 'Chris', 'Jackson', 'Graça', 'Kelly', 'Itamar', 'Neto', 'Andrezza'],
    'Produto': ['Melancia', 'Morango', 'Banana', 'Maracujá', 'Coco', 'Laranja', 'Manga', 'Uva', 'Pera', 'Amora'],
    'Quantidade': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Valor': [12.0, 34.3, 25.0, 10.0, 23.0, 43.2, 44.0, 32.0, 21.0, 21.0]
}

# print(controle_vendas)
fm1 = pd.DataFrame(dict_vendas)
print(fm1)
