import numpy as np


arr = np.random.randint(1, 101, (5, 5))


print("Matrix:")
print(arr)


print("\n Diagonal Elements:")
print(arr.diagonal())


print("\n Elements Greater Than 50:")
print(arr[arr > 50])


arr[arr < 30] = 0

# Print modified array
print("\n Modified Array:")
print(arr)