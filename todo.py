import tkinter as tk
from tkinter import messagebox, simpledialog
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Create UI components
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack()

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.complete_btn = tk.Button(root, text="Mark as Complete", command=self.mark_complete)
        self.complete_btn.pack()

        self.delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack()

        self.save_btn = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_btn.pack()

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_complete(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            if not task.startswith("[Done] "):
                self.tasks[index] = "[Done] " + task
                self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
            self.update_listbox()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
