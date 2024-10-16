import numpy as np

arr = np.array([12,34,5,6,77,6,44,3])

#Retorna o valor máximo de um array
maximo = np.max(arr)
print(f"Valor máximo do array: {maximo}")

#Retorna o valor nínimo de um array
minimo = np.min(arr)
print(f"Valor Mínimo do array: {minimo}")

#Retorna o valor médio dos elementos de um array
media = np.mean(arr)
print(f"Média dos valores do array: {media}")

#Retorna o desvio padrão do array
desvio_padrao = np.std(arr)
print(f"Desvio padrão do array: {desvio_padrao}")

#Retorna a soma dos elementos de um array
soma = np.sum(arr)
print(f"Soma dos valores do array: {soma}")