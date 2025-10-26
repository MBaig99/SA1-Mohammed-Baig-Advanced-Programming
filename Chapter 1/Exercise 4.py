#-------------Exercise 4-------------

# This program asks the user for 3 numbers and will print the largest one


# Ask user for 3 numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


# Here program compares the 3 numbers

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3


# Output!!!

print(f"The largest number is: {largest}!")
