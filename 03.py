import numpy as np


arr = np.random.randint(20, 81, (4, 5))

print("Matrix:")
print(arr)

print("Minimum Value:", arr.min())
print("Maximum Value:", arr.max())

print("Sum:", arr.sum())

print("Mean:", arr.mean())

print("Standard Deviation:", arr.std())


print("Row Sum:", arr.sum(axis=1))

print("Column Sum:", arr.sum(axis=0))
