import tkinter as tk
from tkinter import messagebox
import pickle

# Functions
def add_task():
    task = task_entry.get().strip()
    if task:
        task_list.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    selected_items = listbox.curselection()
    if selected_items:
        # Convert to list and reverse to prevent index shifting issues
        for index in reversed(list(selected_items)):
            if index < len(task_list):
                del task_list[index]
                listbox.delete(index)
    else:
        messagebox.showwarning("Warning", "Select at least one task to remove!")

def mark_done():
    selected_item = listbox.curselection()
    if selected_item:
        index = selected_item[0]
        if index < len(task_list):  # ensure index exists
            item = task_list[index]

            # toggle checkmark
            if item.startswith("✅"):
                task_list[index] = item[1:]  # remove checkmark
            else:
                task_list[index] = item + "✅"  # add checkmark

            # update listbox
            listbox.delete(index)
            listbox.insert(index, task_list[index])
    else:
        messagebox.showwarning("Warning", "Select a Task to Mark as Done!")

def save_tasks():
    with open("tasks.pkl", "wb") as f:
        pickle.dump(task_list, f)
    messagebox.showinfo("Success", "Tasks Saved Successfully!")

def load_tasks():
    global task_list
    try:
        with open("tasks.pkl", "rb") as f:
            task_list = pickle.load(f)
            listbox.delete(0, tk.END)  # clear Listbox before loading
            for task in task_list:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        task_list = []
    except Exception as e:
        messagebox.showerror("Error", f"Failed to Load Tasks: {e}")

# main application Window
app = tk.Tk()
app.title("To-Do List")
app.geometry("390x530")
app.config(bg="#242424")

# task list Storage
task_list = []

# title label
title = tk.Label(app, text="To-Do List", font=("Impact", 18), bg="#242424", fg="#fff")
title.pack(pady=10)

# task entry
task_entry = tk.Entry(app, width=35, font=("Arial", 12))
task_entry.pack(pady=10)

# buttons
button_frame = tk.Frame(app, bg="#242424")
button_frame.pack()

add_button = tk.Button(button_frame, text="Add", width=10, font=("Arial", 10), command=add_task)
add_button.grid(row=0, column=0, padx=5)

remove_button = tk.Button(button_frame, text="Remove", width=10, font=("Arial", 10), command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

mark_button = tk.Button(button_frame, text="Mark Done", width=10, font=("Arial", 10), command=mark_done)
mark_button.grid(row=1, column=0, padx=5, pady=5)

save_button = tk.Button(button_frame, text="Save", width=10, font=("Arial", 10), command=save_tasks)
save_button.grid(row=1, column=1, padx=5, pady=5)

load_button = tk.Button(button_frame, text="Load", width=10, font=("Arial", 10), command=load_tasks)
load_button.grid(row=1, column=2, padx=5, pady=5)



# task listbox
listbox = tk.Listbox(app, height=15, width=35, font=("Consolas", 12), selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

# run app
app.mainloop()
