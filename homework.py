import numpy as np

array = [1, 3, 8, 3, 5, 4, 3, 4, 0, 7, 8, 6, 5, 4, 7, 6, 2, 4, 3, 2, 3, 3 , 5, 6]

array = np.array(array)


array2 = array.reshape(2, 12)
array3 = array.reshape(1, 24)
array4 = array.reshape(3, 8)
array5 = array.reshape(4, 6)



print(array2)
print(array3)
print(array5)
print(array4)
