#--------------Exercise 3---------------

# This exercise asks us create a program that check whether 3 side lengths can form a triangle



# Here i ask user to input 3 lengths
a = float(input("Enter length of side 1: "))
b = float(input("Enter length of side 2: "))
c = float(input("Enter length of side 3: "))


# Now i apple the triangle inequality rule

# The triangle is valid if:

# a + b >= c , a + c >= b , b + c >= a

if a + b >= c and a + c >= b and b + c >= a:
    print("Yes, these 3 sides can form a triangle!")
else:
    print("No, these sides CANNOT form a triangle!")
