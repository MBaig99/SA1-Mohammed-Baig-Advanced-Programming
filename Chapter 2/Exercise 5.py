#=========================== Exercise 5 =============================#

# Develop a GUI to perform basic arithmetic operations like addition, subtraction, multiplication, Division, and modulo division using buttons. You can ask the user to enter the values in entry widget and select the operation to be performed.


import tkinter as tk
from tkinter import messagebox

# Setting up main window

window= tk.Tk()
window.title("Simple Calculator")
window.geometry("300x220")
window.resizable(False, False)


# Input Fields

tk.Label(window, text="Enter number 1:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
num1_entry = tk.Entry(window)
num1_entry.grid(row=0, column=1)
    

tk.Label(window, text="Enter number 2:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
num2_entry = tk.Entry(window)
num2_entry.grid(row=1, column=1)


# Result Label
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=2, column=0, columnspan=2, pady=10)


# Calculator Functions
def calculate(op):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
            
        result_label.config(text=f"Result: {result}")
        
    except ValueError:
        messagebox.showerror("Error, Please enter valid numbers!")
        
        
# Operation Buttons

tk.Button(window, text="+", width=5, command=lambda: calculate("+")).grid(row=3, column=0, pady=5)
tk.Button(window, text="-", width=5, command=lambda: calculate("-")).grid(row=3, column=1, pady=5)
tk.Button(window, text="*", width=5, command=lambda: calculate("*")).grid(row=4, column=0, pady=5)
tk.Button(window, text="/", width=5, command=lambda: calculate("/")).grid(row=4, column=1, pady=5)
tk.Button(window, text="%", width=5, command=lambda: calculate("%")).grid(row=5, column=0, columnspan=2, pady=5)


window.mainloop()

    
