 # Further Bonus Exercise II: Capitalize letters
 
 
import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Uppercase Converter")
root.geometry("350x200")

# Label
label = ttk.Label(root, text="Enter text:")
label.pack(pady=10)

# Entry box for input
entry = ttk.Entry(root, width=40)
entry.pack(pady=5)

# Output label
result_label = ttk.Label(root, text="", foreground="blue")
result_label.pack(pady=10)

# convert text to uppercase
def convert_to_upper():
    text = entry.get()
    result_label.config(text=text.upper())

# Button
convert_btn = ttk.Button(root, text="Convert to UPPERCASE", command=convert_to_upper)
convert_btn.pack(pady=10)

# Run main loop
root.mainloop()
