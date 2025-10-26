# ========== Exercise 2: Coffee Vending Machine ☑️ ========== #

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  

# ----- Main Window -----
window = tk.Tk()
window.title("Coffee Vending Machine")
window.geometry("380x440")
window.resizable(False, False)

try:
    img = Image.open("coffee.jpg")      
    img = img.resize((140, 140))        
    coffee_img = ImageTk.PhotoImage(img)
    tk.Label(window, image=coffee_img).grid(row=0, column=0, columnspan=2, pady=8)
except Exception as e:
    # If image fails, There is a placeholder text
    tk.Label(window, text="[coffee.jpg not found]").grid(row=0, column=0, columnspan=2, pady=8)
    print("Image load error:", e)

# ----- Coffee Selection -----
tk.Label(window, text="Select Coffee:").grid(row=1, column=0, sticky="w", padx=10, pady=5)

coffee_var = tk.StringVar(value="Espresso")
tk.Radiobutton(window, text="Espresso (8 AED)",   value="Espresso",   variable=coffee_var)\
    .grid(row=2, column=0, sticky="w", padx=20)
tk.Radiobutton(window, text="Cappuccino (10 AED)", value="Cappuccino", variable=coffee_var)\
    .grid(row=3, column=0, sticky="w", padx=20)
tk.Radiobutton(window, text="Latte (12 AED)",     value="Latte",      variable=coffee_var)\
    .grid(row=4, column=0, sticky="w", padx=20)

# ----- Add-ons -----
tk.Label(window, text="Add-ons:").grid(row=5, column=0, sticky="w", padx=10, pady=(10, 0))
sugar_var = tk.BooleanVar(value=False)
milk_var  = tk.BooleanVar(value=False)
tk.Checkbutton(window, text="Sugar", variable=sugar_var).grid(row=6, column=0, sticky="w", padx=20)
tk.Checkbutton(window, text="Milk",  variable=milk_var ).grid(row=7, column=0, sticky="w", padx=20)

# ----- Money Entry -----
tk.Label(window, text="Insert money (AED):").grid(row=8, column=0, sticky="w", padx=10, pady=8)
money_entry = tk.Entry(window, width=18)
money_entry.grid(row=9, column=0, sticky="w", padx=10)

# ----- Pricing -----
prices = {"Espresso": 8, "Cappuccino": 10, "Latte": 12}

# ----- Actions -----
def place_order():
    coffee = coffee_var.get()
    price = prices.get(coffee, 0)

    try:
        money = float(money_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount of money!")
        return

    if money < price:
        messagebox.showwarning("Insufficient", f"{coffee} costs {price} AED. You entered {money:.2f} AED.")
        return

    addons = []
    if sugar_var.get(): addons.append("Sugar")
    if milk_var.get():  addons.append("Milk")
    addons_text = ", ".join(addons) if addons else "None"

    change = money - price
    messagebox.showinfo(
        "Order Confirmed",
        f"Your {coffee} is ready!\n"
        f"Add-ons: {addons_text}\n\n"
        f"Total: {price} AED\n"
        f"Change: {change:.2f} AED"
    )

def clear_all():
    coffee_var.set("Espresso")
    sugar_var.set(False)
    milk_var.set(False)
    money_entry.delete(0, "end")

# ----- Buttons (outside functions!) -----
tk.Button(window, text="Order", width=10, command=place_order)\
    .grid(row=10, column=0, pady=12, sticky="w", padx=10)
tk.Button(window, text="Clear", width=10, command=clear_all)\
    .grid(row=10, column=0, pady=12, sticky="e", padx=10)

window.mainloop()

    
