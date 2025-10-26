#----------------------------------------Exercise 12------------------------------------------

# This program calculates the areas of 3 different shapes


import math

# Function for square area

def area_square():
    side = float(input("Enter the length of the square's side: "))
    area = side * side
    print(f"The area of the square is: {area}")


# Function to calculate circle area
def area_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    print(f"The area of the circle is: {area}")


# Function to calculate triangle area
def area_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area}")


# Main menu for selection of shape
print("AREA CALC")
print("1. Area of a Circle")
print("2. Area of a Square")
print("3. Area of a Triangle")


choice = input("Choose an option (1-3): ")

if choice == "1":
    area_circle()
elif choice == "2":
    area_square()
elif choice == "3":
    area_triangle()
else: 
    print("Invalid Option Selected.")
