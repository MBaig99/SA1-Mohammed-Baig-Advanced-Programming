#---------------------------Exercise 5---------------------------------

# This program keeps looping as long as the user enters 'Y' key
# And also counts the amount of loops
# IMPORANT: if you want to run this code you must enter 'Y' not 'y' and vice versa for 'N'


count = 0 # This keeps track of how many times the loop goes
choice = input("Would you like to continue? (Y/N): ")


# Loop goes on while user choses 'Y'
while choice == 'Y':
    count += 1
    choice = input("Would you like to continue? (Y/N): ")

# When the user enters anything other than 'Y'
print(f"\nThe loop ran {count} time(s)!")
