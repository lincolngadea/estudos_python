import numpy as np

arr = np.array([1,2,3])
print(arr)
print(arr[1])
print(arr[-1])
print(arr[2])

arr = np.array([1,2,3,4,5,6])
arr_new = arr.reshape(2,3)
#Transforma um array em matrizes... com 2 linhas e 3 colunas

print(f'Array unidirecional {arr}')
print(f'Array bidirecional \n{arr_new}')

#acessando elementos da matriz
print(f'Acessar o segundo elemento do array 1: {arr_new[0,1]}')
print(f'Acessar o segundo elemento do array 2: {arr_new[1,1]}')

#Op. matemáticas de um Array com numpy

arr_soma = arr + arr

print(arr_soma)
