import tkinter as tk

# Creating a main window
window = tk.Tk()
window.title("Login Page")
window.geometry("300x150")
window.resizable(False, False)

# Username Label
username_label = tk.Label(window, text="Username: ")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Username Entry
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password Label
password_label = tk.Label(window, text="Password: ")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

# Password Entry
password_entry = tk.Entry(window)
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login Button
login_button = tk.Button(window, text="Login")
login_button.grid(row=2, column=1, pady=10, sticky="e")

window.mainloop()
