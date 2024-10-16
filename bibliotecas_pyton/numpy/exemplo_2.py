import numpy as np

#Criando arrays sequenciais

arr_a = np.arange(20) #
print(f'sequencia de 0 a 19 {arr_a}')

arr_b = np.arange(1,11) #
print(f'intercalando valores do array de 1 a 10 {arr_b}')

arr_c = np.arange(0,21,2)
print(f'Sequência com intervalos de 2: {arr_c}')

arr_zeros = np.zeros(3)
print(f'Cria um array com 3 Zeros: {arr_zeros}')

arr_zeros_2 = np.zeros((4,4))
print(f'Cria uma matriz de 4 arrays com 4 Zeros: \n{arr_zeros_2}')

arr_one = np.ones((4,4))
print(f'Cria uma matriz de 4 arrays com 4 ums: \n{arr_one}')

#Uma matriz identidade é uma matriz quadrada em que todos os elementos da diagonal principal são iguais a 1 e todos os
#outros elementos são iguais a 0.

arr_eye = np.eye(4,4)
print(f'Matriz com eye:\n{arr_eye}')


# Gera um array com valores aleatórios entre 0 e 1.
rand_1 = np.random.rand(4)
print(rand_1)