#----------------------Exercise 9-----------------------------


# This program asks us to create several operations with an integer list


# Number list
numbers = [12,5,33,8,9,19,28,50,2,10]


# Output list using a loop

print("Original List:")
for num in numbers:
    print(num, end=" ")
print("\n") # line breaking


# Output the highest and lowest integer
print(f"Highest Value: {max(numbers)}")
print(f"Lowest Value: {min(numbers)}\n")


# Sorting the numbers out in descending order
numbers.sort(reverse=True)
print("\nList in Descending Order:")
print(numbers)


# Append 2 numbers into the list
numbers.append(67)
numbers.append(41)


# Finally printing the list after appending

print("\nThe list after appending 67 and 41: ")
print(numbers)
