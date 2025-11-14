#Write a Python program to count how many times a particular element appears in a list.
numbers = [1, 2, 3, 2, 4, 2, 5]

x = int(input("Enter number to count: "))
count = numbers.count(x)

print("Count:", count)
