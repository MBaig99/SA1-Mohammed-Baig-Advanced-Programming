#----------------------------Exercise 7----------------------------

# This program prints all even numbers from 1 to 100


for num in range(1, 101):

    # If the number is odd, it skips
    if num % 2 != 0:
        continue

    # If it is even, it prints
    print(num)
