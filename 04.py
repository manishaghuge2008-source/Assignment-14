import numpy as np


arr = np.arange(1, 25)


a = arr.reshape(4, 6)
b = arr.reshape(3, 8)
c = arr.reshape(2, 3, 4)


print("Original Array:")
print(arr)
print("Shape:", arr.shape)

print("\n  4 x 6 Array:")
print(a)
print("Shape:", a.shape)

print("\n  3 x 8 Array:")
print(b)
print("Shape:", b.shape)

print("\n  2 x 3 x 4 Array:")
print(c)
print("Shape:", c.shape)