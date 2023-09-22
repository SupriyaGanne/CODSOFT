import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter any task.")


def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select any task to delete.")


def update_task():
    try:
        index = listbox.curselection()
        updated_task = entry.get()
        if updated_task:
            listbox.delete(index)
            listbox.insert(index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except:
        messagebox.showwarning("Warning", "Please select any task to update.")


def mark_as_done():
    try:
        index = listbox.curselection()
        task = listbox.get(index)
        updated_task = task + " (Done)"
        listbox.delete(index)
        listbox.insert(index, updated_task)
    except:
        messagebox.showwarning("Warning", "Please select any task to mark as done.")


window = tk.Tk()
window.title("To-Do List")



listbox = tk.Listbox(window, width=50, height=10, font=("san-sefir", 12),bg="#12486B",fg="white")
listbox.pack(pady=20)


scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


entry = tk.Entry(window, font=("san-serif", 12) ,bg="#419197" ,fg="white")
entry.pack(pady=20)


add_button = tk.Button(window, text="Add a Task", command=add_task ,bg="#78D6C6", fg="white")
add_button.pack(pady=10)
delete_button = tk.Button(window, text="Delete a Task", command=delete_task,bg="#78D6C6", fg="white")
delete_button.pack(pady=10)
update_button = tk.Button(window, text="Update a Task", command=update_task,bg="#78D6C6", fg="white")
update_button.pack(pady=10)
mark_done_button = tk.Button(window, text="Mark as Done", command=mark_as_done,bg="#78D6C6", fg="white")
mark_done_button.pack(pady=10)

window.configure(bg="#FAF2D3")
window.mainloop()
