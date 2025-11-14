# Write a Python program to display only even numbers from a given list.
numbers = [10, 15, 22, 33, 40, 55, 60]

print("Even numbers:")
for n in numbers:
    if n % 2 == 0:
        print(n)
