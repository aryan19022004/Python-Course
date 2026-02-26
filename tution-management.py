import tkinter as tk
from tkinter import messagebox
import json
import os

# ------------------ File Setup ------------------

if not os.path.exists("students.json"):
    with open("students.json", "w") as f:
        json.dump([], f)

if not os.path.exists("batches.json"):
    with open("batches.json", "w") as f:
        json.dump([], f)

# ------------------ Functions ------------------

def load_batches():
    with open("batches.json", "r") as f:
        return json.load(f)

def save_batches(data):
    with open("batches.json", "w") as f:
        json.dump(data, f, indent=4)

def load_students():
    with open("students.json", "r") as f:
        return json.load(f)

def save_students(data):
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)

# ------------------ Batch Management ------------------

def add_batch():
    batch_name = batch_entry.get()
    start = start_entry.get()
    end = end_entry.get()

    if batch_name == "":
        messagebox.showerror("Error", "Enter Batch Name")
        return

    batches = load_batches()
    batches.append({
        "batch_name": batch_name,
        "start_time": start,
        "end_time": end
    })
    save_batches(batches)
    messagebox.showinfo("Success", "Batch Added")
    update_batch_menu()

def delete_batch():
    selected = batch_var.get()
    batches = load_batches()
    batches = [b for b in batches if b["batch_name"] != selected]
    save_batches(batches)
    messagebox.showinfo("Deleted", "Batch Deleted")
    update_batch_menu()

def update_batch_menu():
    batches = load_batches()
    menu = batch_menu["menu"]
    menu.delete(0, "end")
    for b in batches:
        menu.add_command(label=b["batch_name"],
                         command=lambda value=b["batch_name"]: batch_var.set(value))

# ------------------ Student Management ------------------

def add_student():
    name = student_name_entry.get()
    batch = batch_var.get()
    fee = fee_entry.get()

    if name == "" or batch == "":
        messagebox.showerror("Error", "Fill all details")
        return

    students = load_students()
    students.append({
        "name": name,
        "batch": batch,
        "monthly_fee": fee,
        "fees_paid": {}
    })
    save_students(students)
    messagebox.showinfo("Success", "Student Added")

def view_students():
    students = load_students()
    output = ""
    for s in students:
        output += f"Name: {s['name']} | Batch: {s['batch']} | Fee: {s['monthly_fee']}\n"
    messagebox.showinfo("Students", output if output else "No Students Found")

# ------------------ GUI ------------------

root = tk.Tk()
root.title("Tuition Management System")
root.geometry("500x500")

# ----- Batch Section -----

tk.Label(root, text="Batch Management", font=("Arial", 14)).pack(pady=5)

batch_entry = tk.Entry(root)
batch_entry.pack()
batch_entry.insert(0, "Batch Name")

start_entry = tk.Entry(root)
start_entry.pack()
start_entry.insert(0, "Start Time")

end_entry = tk.Entry(root)
end_entry.pack()
end_entry.insert(0, "End Time")

tk.Button(root, text="Add Batch", command=add_batch).pack(pady=5)
tk.Button(root, text="Delete Batch", command=delete_batch).pack(pady=5)

# ----- Student Section -----

tk.Label(root, text="Student Admission", font=("Arial", 14)).pack(pady=10)

student_name_entry = tk.Entry(root)
student_name_entry.pack()
student_name_entry.insert(0, "Student Name")

batch_var = tk.StringVar(root)
batch_var.set("Select Batch")

batch_menu = tk.OptionMenu(root, batch_var, "")
batch_menu.pack()

fee_entry = tk.Entry(root)
fee_entry.pack()
fee_entry.insert(0, "Monthly Fee")

tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)

update_batch_menu()

root.mainloop()