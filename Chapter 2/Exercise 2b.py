#============================================Exercise 2B===============================================


# Exercise 2 b: Square Grid ☑️


import tkinter as tk

window = tk.Tk()
window.title("GUI PACK EXAMPLE")
window.geometry('400x300')


# Left Frame
left_frame = tk.Frame(window, bd=5, relief="ridge", bg="black")
left_frame.pack(side='left', fill="both", expand=True)


# Right Frame 
right_frame = tk.Frame(window, bd=5, relief="ridge")
right_frame.pack(side="right", fill="both", expand=True)


# Label A (TOP LEFT)
label_A = tk.Label(left_frame, text="A", bg="#1A1D2E", fg="white")
label_A.pack(side="top", fill="both", expand=True)


# Label B (BOTTOM LEFT)
label_B = tk.Label(left_frame, text="B", bg="white", fg="black")
label_B.pack(side='bottom', fill="both", expand=True)


# Label C (TOP RIGHT)
label_C = tk.Label(right_frame, text="C", bg="white", fg="black")
label_C.pack(side="top", fill="both", expand=True)


# Label D (BOTTOM RIGHT)
label_D = tk.Label(right_frame, text="D", bg="#1A1D2E", fg="white")
label_D.pack(side="bottom", fill="both", expand=True)

window.mainloop()
