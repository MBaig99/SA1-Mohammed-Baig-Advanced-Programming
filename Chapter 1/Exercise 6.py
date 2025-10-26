#--------------------------Exercise 6------------------------

# This program prints numbers from 0-100
# For multiples of 3 print "Fizz"
# For multiples of 5 print "Buzz"
# For multiples of 3 and 5 print "FizzBuzz"



for num in range(1,101):

    # Checks multiples of 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    # Checks multiples of 3
    elif num % 3 == 0:
        print("Fizz")

    # Checks multiples of 5
    elif num % 5 == 0:
        print("Buzz")

    # Other numbers willl print normally
    else:
        print(num)
