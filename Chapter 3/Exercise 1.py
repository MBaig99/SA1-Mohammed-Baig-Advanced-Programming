# =================== Exercise 1: Greeting App ☑️ ===================== #

# Exercise 1: Greeting App ☑️
# Develop a GUI to greet the user. The app should have two frames: InputFrame and DisplayFrame.


import tkinter as tk
from tkinter import ttk


# Setting up main window
window = tk.Tk()
window.title("Baig's Greeting App")
window.geometry("400x250")
window.resizable(False, False)


# ----- Frames ----- #
input_frame = tk.Frame(window, bg="#d1e7ff") # Light Blue Color
input_frame.pack(fill="x")

display_frame = tk.Frame(window, bg="#f5f5f5") # Light Gray Color
display_frame.pack(fill="both", expand=True)


# ---- Input Frame Widgets ---- #

# Title Label
title_label = tk.Label(input_frame, text="Greeting App", font=("Arial", 14, "bold"), bg="#d1e7ff", fg="blue")
title_label.grid(row=0,column=0,pady=5)


# Name Entry
tk.Label(input_frame, text="Enter your name:", bg="#d1e7ff").grid(row=1, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(input_frame, width=25)
name_entry.grid(row=1, column=1, pady=5)


# Color Dropdown
tk.Label(input_frame, text="Select Color:", bg="#d1e7ff").grid(row=2, column=0, padx=10, pady=5, sticky="e")
color_var = tk.StringVar()
color_menu = ttk.Combobox(input_frame, textvariable=color_var, values=["Red", "Green", "Blue", "Purple"],state='readonly', width=22)
color_menu.grid(row=2, column=1, pady=5)


# ----- Display Frame Label ----- #
greeting_label = tk.Label(display_frame, text="", font=("Arial", 14), bg="#f5f5f5")
greeting_label.pack(pady=30)


# ----- Button Logic ----- #
def update_greeting():
    name = name_entry.get()
    color = color_var.get()
    
    if name and color: # It will only update if both name and color fields are updated
        greeting_label.config(text=f"Hello, {name}!", fg=color.lower())
        
# Button
update_btn = tk.Button(input_frame, text="Update Greeting", command=update_greeting)
update_btn.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
