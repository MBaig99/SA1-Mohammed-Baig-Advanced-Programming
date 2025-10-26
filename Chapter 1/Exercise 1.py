#----------Exercise 1---------------

# This exercise asked me to ask for user's name and age, format the name and count the length of user's name and add the age by 1


# To ask for user's name

print("Hello User!")
name = input("What is your name?\n")


# To ask for user's age

age = input("What is your age?\n")


# Format user's name using title()

formatted_name = name.title()


# This is where i print the greet with formatted name

print(f"It is nice to meet you, {formatted_name}")


# This part prints the length of the user's name

print("The length of your name is:")
print(len(name))


# Here it takes user's age as integer and adds it by 1, showing result

print(f"You will be {int(age) + 1} in a year.")
