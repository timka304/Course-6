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

#SLICING

numbers1 = np.array(numbers)

print(numbers1[0:5])

print(numbers1[0:7:2])

print(numbers1[[0, 1, 3, 4, 5]])

print(numbers[5:15])

print(numbers1[numbers1>5])

print(numbers1[(numbers1%2)==0])


numbers3 = np.arange(1, 25)
numbers4 = numbers3.reshape(6, 4)

print(numbers4)

print(numbers4[2:5, 1:3])

print(np.random.permutation(numbers4))


rand1 = np.random.randint(1, 100, 10)
rand2 = np.random.randint(1, 100, 10)

print(rand1)
print(np.sort(rand1))

print(rand1*5)
print(rand2)
print(rand2*5)

print(rand1 + rand2)
print(rand1/rand2)
print(rand1*rand2)
print(rand1-rand2)