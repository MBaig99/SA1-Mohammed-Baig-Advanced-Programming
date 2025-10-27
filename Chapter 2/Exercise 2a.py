#======================================= Exercise 2A ==========================================#

 # Exercise 2 a: Using pack ☑️

import tkinter as tk

window = tk.Tk()
window.title("GUI Pack Example")
window.geometry("500x200")

# Label A (Top)
label_A = tk.Label(window, text="A", bg="red", bd=5, relief="ridge")
label_A.pack(fill="x", padx=5, pady=5)  

# Frame for C and D (middle row)
middle_frame = tk.Frame(window, bg="lightgray")
middle_frame.pack(fill="x")

label_C = tk.Label(middle_frame, text="C", bg="blue", fg="white", bd=5, relief="sunken")
label_C.pack(side="left", padx=5)       

label_D = tk.Label(middle_frame, text="D", bg="white", bd=5, relief="raised")
label_D.pack(side="right", padx=5)

# Frame for B (bottom row)
bottom_frame = tk.Frame(window, bg="lightgray")
bottom_frame.pack(fill="x", pady=5)

label_B = tk.Label(bottom_frame, text="B", bg="yellow", bd=5, relief="groove")
label_B.pack()                          

window.mainloop()
