# =============== Exercise 4: Draw Shape☑️ ============== #

import tkinter as tk
from tkinter import ttk, messagebox



# Main window
window = tk.Tk()
window.title("Shape Drawer")
window.geometry("450x450")
window.resizable(False, False)


# Shape Selection
tk.Label(window, text="Select Shape:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
shape_var = tk.StringVar(value="Oval")
shape_menu = ttk.Combobox(window, textvariable=shape_var, values=["Oval", "Rectangle", "Square", "Triangle"], width=12, state="readonly")
shape_menu.grid(row=0, column=1, pady=10, sticky="w")


# Coordinate Inputs
tk.Label(window, text="X1:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(window, text="Y1:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(window, text="X2:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
tk.Label(window, text="Y2:").grid(row=4, column=0, padx=10, pady=5, sticky="e")


x1_entry = tk.Entry(window, width=10)
y1_entry = tk.Entry(window, width=10)
x2_entry = tk.Entry(window, width=10)
y2_entry = tk.Entry(window, width=10)


x1_entry.grid(row=1, column=1, pady=5, sticky="w")
y1_entry.grid(row=2, column=1, pady=5, sticky="w")
x2_entry.grid(row=3, column=1, pady=5, sticky="w")
y2_entry.grid(row=4, column=1, pady=5, sticky="w")


# Canvas
canvas = tk.Canvas(window, width=350, height=250, bg="white")
canvas.grid(row=6, column=0, columnspan=3, pady=15)


# Draw Function
def draw_shape():
    try:
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid coordinates!")
        return
    
    
    
    canvas.delete("all") # This deletes all previous drawings
    shape = shape_var.get()
    
    
    if shape == "Oval":
        canvas.create_oval(x1, y1, x2, y2, outline="black", width=2)
        
    elif shape == "Rectangle":
        canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)
        
    elif shape == "Square":
        # Make square by using smallest side
        side = min(abs(x2 - x1), abs(y2-y1))
        canvas.create_rectangle(x1, y1, x1 + side,  y1 + side, outline="black", width=2)
        
    elif shape == "Triangle":
        mid = (x1 + x2) // 2
        canvas.create_polygon(mid, y1, x1, y2, x2, y2, outline="black", fill="", width=2)
        
# Draw Button
tk.Button(window, text="Draw Shape", command=draw_shape).grid(row=5, column=0, columnspan=3, pady=5)


window.mainloop()
