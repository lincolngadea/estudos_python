import numpy as np

arr = np.arange(12)
print(f"Array com Arange: {arr}")

arr2 = arr.reshape(3,4)
print(f"Array com reshape: \n{arr2}")

arr_t  = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Array normal: \n{arr_t}")

arr_result = np.transpose(arr_t) #Transforma o array na vertical
print(f"Array com Transpose \n{arr_result}")

#Concatenacao de Array
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np .array([[7,8,9],[10,11,12]])

#Por coluna
arr_concat = np.concat((arr1,arr2),axis=1)
print(f"Array Concatenado por coluna: \n{arr_concat}")

#Por Linha
arr_concat = np.concat((arr1,arr2),axis=0)
print(f"Array Concatenado por linha: \n{arr_concat}")

#Divide array em dois
arr = np.array([1,2,3,4,5,6])
arr_div = np.split(arr,2)
print(f"Array dividido: {arr_div}")