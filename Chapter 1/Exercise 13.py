#---------------------------------------Exercise 13---------------------------------------------------

# This program calculates product of all values from a list



# This func calculates the products of list items

def product_of_list(values):
    product = 1
    for num in values:
        product *= num # It will multiply each value into product
    return product


# Main Program
numbers = [2, 3, 4, 5] 

result = product_of_list(numbers) # Here I call the function and store list


# Result

print(f"The product of the list values is: {result}")
