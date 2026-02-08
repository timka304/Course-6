import numpy as np
import random

numbers = [2, 4, 5, 8, 10, 12, 21, 34, 32]

print(numbers)

print(type(numbers))

array = np.array(numbers)

print(type(array))

range1 = np.arange(1, 10, 1)

print(range1)

array2 = np.random.randint(1, 10, (3, 2))
print(array2)

array3 = array2.reshape(2, 3)

print(array3)

var = array3.ndim

print(var)

n = np.zeros((1, 4))

print(n)

e = np.ones((1,6))

print(e)

shape1 = e.shape

line1 = np.linspace(10, 20, 5)

print(line1)