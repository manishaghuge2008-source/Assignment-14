import numpy as np


arr = np.random.randn(6, 6)


print("Matrix:")
print(arr)


print("\n  Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)


print("\n  Index of Maximum Value:", arr.argmax())
print("Index of Minimum Value:", arr.argmin())


print("\n  Top-left 3x3 Submatrix:")
print(arr[:3, :3])


arr = np.abs(arr)


print("\n  Modified Matrix:")
print(arr)


print("\n  Mean:", arr.mean())

