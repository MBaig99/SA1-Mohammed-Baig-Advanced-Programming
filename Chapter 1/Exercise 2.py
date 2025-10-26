#----------------------Exercise 2---------------------

# This exercise asks the user for 2 integers and print basic arithmetic outputs.


# This part asks user to input 2 digits
num1 = int(input("Enter your first digit: "))
num2 = int(input("Enter your second digit: "))


# Here it does calculations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
quot_result = num1 / num2
rem_result = num1 % num2


# Display Results
print("-------RESULTS----------")
print(f"Sum(+): {sum_result}")
print(f"Difference(-): {diff_result}")
print(f"Prodcut(*): {prod_result}")
print(f"Quotient(/): {quot_result}")
print(f"Remainder(%): {rem_result}")
