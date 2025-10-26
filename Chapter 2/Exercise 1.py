#============================== Exercise 1 ======================================#

# Develop a GUI program to do the following using the tkinter module



import tkinter as tk

# Creating the main window
window = tk.Tk()
window.title("Welcome App")


# I set the default window size
window.geometry("400x200") # Width and Height


# Disable window resizing
window.resizable(False, False)


# Setting BG color
window.config(bg = "lightblue")


# Here I create a welcome label with font adjustments
welcome_label = tk.Label(window,
                         text="Welcome to my App!",
                         font=("Arial" ,20, "bold"),
                         bg = "lightblue")
welcome_label.pack(pady=50) # add padding y


# I run the window
window.mainloop()
