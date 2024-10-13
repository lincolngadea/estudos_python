import numpy as np

arr = np.arange(12)
print(f"Array com Arange: {arr}")

arr2 = arr.reshape(3,4)
print(f"Array com reshape: \n{arr2}")

arr_t  = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Array normal: \n{arr_t}")

arr_result = np.transpose(arr_t)
print(f"Array com Transpose \n{arr_result}")
