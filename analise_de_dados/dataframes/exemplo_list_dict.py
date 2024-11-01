import pandas as pd

list_dict = []

registro_1 = {
    'Nome':'Lincoln',
    'Idade':43,
    'Cidade':'Salvador'
}

registro_2 = {
    'Nome':'Rafael',
    'Idade':20,
    'Cidade':'São Paulo'
}

list_dict.append(registro_1)
list_dict.append(registro_2)

data_frame = pd.DataFrame(list_dict)

print(data_frame)


