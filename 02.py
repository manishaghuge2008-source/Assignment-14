import numpy as np

arr = np.random.randint(1, 51, 20)

print("Array:")
print(arr)


print("Minimum Value:", arr.min())
print("Index of Minimum Value:", arr.argmin())

print("Maximum Value:", arr.max())
print("Index of Maximum Value:", arr.argmax())

print("Sum:", arr.sum())

print("Mean:", arr.mean())

print("Standard Deviation:", arr.std())