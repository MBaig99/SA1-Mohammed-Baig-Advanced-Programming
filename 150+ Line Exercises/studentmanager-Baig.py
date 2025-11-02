# ========== Exercise 3: Student Manager ( With Extension 5 - 8) ========== #

# Mohammed Baig
# This program manages student records using GUI Tkinter
# It allows you to view, add, delete, update and sort, student data from a Marks.txt file.



import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext


# ---------- Helper Functions ---------- #


def loadData(filename="Marks.txt"):
    studList = []
    with open(filename, "r") as f:
        lines = f.readlines()[1:]  # Skip first line (total number)
        for line in lines:
            if line.strip():
                parts = [p.strip() for p in line.split(",")]
                stud = {
                    "code": parts[0],
                    "name": parts[1],
                    "marks": list(map(int, parts[2:])),
                }
                studList.append(stud)
    return studList



def saveData(studList, filename="Marks.txt"):
    with open(filename, "w") as f:
        f.write(str(len(studList)) + "\n")
        for s in studList:
            f.write(f"{s['code']}, {s['name']}, {','.join(map(str, s['marks']))}\n")
            
            
# --------- Helpers Calculations ---------- #

def calcGrade(stud):
    cw = sum(stud["marks"][:3])
    exam = stud["marks"][3]
    percent = round(((cw + exam)/ 160) * 100,2)
    if percent >= 70:
        grade = "A"
    elif percent >= 60:
        grade = "B"
    elif percent >= 50:
        grade = "C"
    elif percent >= 40:
        grade = "D"
    else:
        grade = "F"
    return cw, exam, percent, grade



def formatStud(stud):
    cw, exam, per, grade = calcGrade(stud)
    info = f"Name: {stud['name']}\n"
    info += f"Number: {stud['code']}\n"
    info += f"Coursework Total: {cw}\n"
    info += f"Exam Mark: {exam}\n"
    info += f"Overall Percentage: {per}%\n"
    info += f"Grade: {grade}\n"
    return info



# ---------- GUI Functions ----------- #

def clearOutput():
    txtBox.delete(1.0, tk.END)
    
    
def viewAll():
    clearOutput()
    total = 0
    for s in studList:
        txtBox.insert(tk.END, formatStud(s) + "\n")
        total += calcGrade(s)[2]
    avg = round(total / len(studList), 2)
    txtBox.insert(tk.END, f"\nTotal Students: {len(studList)}\nAverage Percentage: {avg}%\n")
    
def viewOne():
    clearOutput()
    code = entryStud.get().strip()
    for s in studList:
        if s["code"] == code or s["name"].lower() == code.lower():
            txtBox.insert(tk.END, formatStud(s))
            return
    messagebox.showinfo("Not Found", "No record found for that student.")
    
    
def showTop():
    clearOutput()
    best = max(studList, key=lambda s: sum(s["marks"]))
    txtBox.insert(tk.END, "Top Student:\n\n" + formatStud(best))
    
def showLow():
    clearOutput()
    low = min(studList, key=lambda s: sum(s["marks"]))
    txtBox.insert(tk.END, "Lowest Student:\n\n" + formatStud(low))
    
def sortAsc():
    studList.sort(key=lambda s: sum(s["marks"]))
    saveData(studList)
    messagebox.showinfo("Sorted", "Students sorted (Low -> High).")
    viewAll()
    
def sortDesc():
    studList.sort(key=lambda s: sum(s["marks"]), reverse = True)
    saveData(studList)
    messagebox.showinfo("Sorted", "Students sorted (High -> Low).")
    viewAll()
    

def addStud():
    code = simpledialog.askstring("Add Student", "Enter student code:")
    name = simpledialog.askstring("Add Student", "Enter student name:")
    try:
        m1 = int(simpledialog.askstring("Add Student", "Enter Mark 1 (out of 20):"))
        m2 = int(simpledialog.askstring("Add Student", "Enter Mark 2 (out of 20):"))
        m3 = int(simpledialog.askstring("Add Student", "Enter Mark 3 (out of 20):"))
        exam = int(simpledialog.askstring("Add Student", "Enter Exam mark (out of 100):"))
    except:
        messagebox.showerror("Error", "Invalid marks entered.")
        return
    studList.append({"code": code, "name": name, "marks": [m1, m2, m3, exam]})
    saveData(studList)
    messagebox.showinfo("Success", f"Student {name} added successfully.")
    viewAll()
    
def delStud():
    code = simpledialog.askstring("Delete Student", "Enter student code and name:")
    for s in studList:
        if s["code"] == code or s["name"].lower() == code.lower():
            studList.remove(s)
            saveData(studList)
            messagebox.showinfo("Deleted", f"{s['name']} removed from records.")
            viewAll()
            return
    messagebox.showinfo("Not Found", "Student not found.")
    
    
def updateStud():
    code = simpledialog.askstring("Update Student", "Enter student code or name:")
    for s in studList:
        if s["code"] == code or s["name"].lower() == code.lower():
            choice = simpledialog.askstring("Update", "What to update? (name/m1/m2/m3/exam)")
            if choice == "name":
                s["name"] = simpledialog.askstring("Update", "Enter new name:")
            elif choice in ["m1", "m2", "m3", "exam"]:
                idx = {"m1":0, "m2":1, "m3":2, "exam":3}[choice]
                try:
                    s["marks"][idx] = int(simpledialog.askstring("Update", f"Enter new {choice.upper()} value:"))
                except:
                    messagebox.showerror("Error", "Invalid number entered.")
                    return
            saveData(studList)
            messagebox.showinfo("Updated", f"{s['name']}'s record updated.")
            viewAll()
            return
    messagebox.showinfo("Not Found", "Student not found.")
    

# ---------- GUI Setup -------- #


win = tk.Tk()
win.title("Student Manager")
win.geometry("750x500")
win.config(bg="#ebeff2")


title = tk.Label(win, text="Student Manager", font=("Arial", 16, "bold"), bg="#ebeff2")
title.pack(pady=10)


# Top Buttons
frameBtns = tk.Frame(win, bg="#ebeff2")
frameBtns.pack(pady=5)

tk.Button(frameBtns, text="View All", width=16, command=viewAll).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frameBtns, text="Top Student", width=16, command=showTop).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frameBtns, text="Lowest Student", width=16, command=showLow).grid(row=0, column=2, padx=5, pady=5)
tk.Button(frameBtns, text="Sort (Low -> High)", width=16, command=sortAsc).grid(row=0, column=3, padx=5, pady=5)
tk.Button(frameBtns, text="Sort (High -> Low)", width=16, command=sortDesc).grid(row=0, column=4, padx=5, pady=5)
tk.Button(frameBtns, text="Add", width=16, command=addStud).grid(row=1, column=1, padx=5, pady=5)
tk.Button(frameBtns, text="Delete", width=16, command=delStud).grid(row=1, column=2, padx=5, pady=5)
tk.Button(frameBtns, text="Update", width=16, command=updateStud).grid(row=1, column=3, padx=5, pady=5)


# Entry Area

entryFrame = tk.Frame(win, bg="#ebeff2")
entryFrame.pack(pady=10)

tk.Label(entryFrame, text="View Individual Student Record:", bg="#ebeff2").pack(side="left")
entryStud = tk.Entry(entryFrame, width=25)
entryStud.pack(side="left", padx=5)
tk.Button(entryFrame, text="View Record", command=viewOne).pack(side="left")


# Output text area
txtBox = scrolledtext.ScrolledText(win, width=80, height=15, wrap=tk.WORD, font=("Courier New", 10))
txtBox.pack(pady=10)

# start program
studList = loadData()
win.mainloop()
