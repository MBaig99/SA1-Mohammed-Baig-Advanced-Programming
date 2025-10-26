# ========== Exercise 3: Area Function☑️ ========== #

import tkinter as tk
from tkinter import ttk
import math


# Main window
window = tk.Tk()
window.title("Area Calculator")
window.geometry("350x200")
window.resizable(False, False)


# Notebook (Tabs)
notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)


# ========== Tab 1: Circle ========== #
circle_tab = ttk.Frame(notebook)
notebook.add(circle_tab, text="Circle")

tk.Label(circle_tab, text="Radius:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
radius_entry = tk.Entry(circle_tab)
radius_entry.grid(row=0, column=1, padx=5)


circle_result = tk.Label(circle_tab, text="Area: ")
circle_result.grid(row=2, column=0,columnspan=2, pady=10)


def calc_circle():
    try:
        r = float(radius_entry.get())
        area = math.pi * r * r 
        circle_result.config(text=f"Area: {area:.2f}")
    except:
        circle_result.config(text="Area: Invalid Input")
        
tk.Button(circle_tab, text="Calculate", command=calc_circle).grid(row=1, column=0, columnspan=2, pady=5)



# ====== Tab 2: Square ====== #
square_tab = ttk.Frame(notebook)
notebook.add(square_tab, text="Square")


tk.Label(square_tab, text="Side:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
side_entry = tk.Entry(square_tab)
side_entry.grid(row=0, column=1, padx=5)


square_result = tk.Label(square_tab, text="Area: ")
square_result.grid(row=2, column=0, columnspan=2, pady=10)


def calc_square():
    try:
        s = float(side_entry.get())
        area = s * s
        square_result.config(text=f"Area: {area:.2f}")
    except:
        square_result.config(text="Area: Invalid Input")

tk.Button(square_tab, text="Calculate", command=calc_square).grid(row=1, column=0, columnspan=2, pady=5)



# ========== Tab 3: Triangle ========== #
rect_tab = ttk.Frame(notebook)
notebook.add(rect_tab, text="Rectangle")


tk.Label(rect_tab, text="Length:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(rect_tab, text="Width:").grid(row=1, column=0, padx=10, pady=5, sticky="e")


length_entry = tk.Entry(rect_tab)
width_entry = tk.Entry(rect_tab)
length_entry.grid(row=0, column=1, padx=5)
width_entry.grid(row=1, column=1, padx=5)


rect_result = tk.Label(rect_tab, text="Area: ")
rect_result.grid(row=3, column=0, columnspan=2, pady=10)        

def calc_rectangle():
    try:
        l = float(length_entry.get())
        w = float(width_entry.get())
        area = l * w
        rect_result.config(text=f"Area: {area:.2f}")
    except:
        rect_result.config(text="Area: Invalid Input")
        
tk.Button(rect_tab, text="Calculate", command=calc_rectangle).grid(row=2, column=0, columnspan=2, pady=5)


window.mainloop()

