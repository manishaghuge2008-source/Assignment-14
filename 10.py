import numpy as np


marks = np.random.randint(30, 101, (10, 5))

# Print student marks
print("Student Marks:")
print(marks)

# Calculate total marks of each student

total = marks.sum(axis=1)
print("\n  Total Marks:")
print(total)

# Calculate average marks of each student

average = marks.mean(axis=1)
print("\n  Average Marks:")
print(average)

# Find highest and lowest total marks

print("\n   Student with Highest Total:", total.argmax())
print("Student with Lowest Total:", total.argmin())

# Class mean and standard deviation

print("\n  Class Mean:", marks.mean())
print("Class Standard Deviation:", marks.std())

# Reshape array (optional)

new_marks = marks.reshape(5, 10)
print("\n  Reshaped Array (5x10):")
print(new_marks)

# Top 3 students based on total marks

top3 = total.argsort()[-3:]

print("\n  Top 3 Students Index:")
print(top3)

print("\n  " \
"Marks of Top 3 Students:")
print(marks[top3])