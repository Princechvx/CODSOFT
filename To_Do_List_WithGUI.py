"""
To-Do List Application with GUI

This GUI-based application allows users to add, update, delete, and view tasks
from their to-do list in a visually interactive way.
"""

import tkinter as tk
from tkinter import messagebox


class ToDoListApp:
    def __init__(self, root):
        """
        Initializes the To-Do List application.
        """
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")
        self.tasks = {}

        # UI Elements
        self.task_input_label = tk.Label(root, text="Enter Task:", font=("Arial", 12))
        self.task_input_label.pack(pady=5)

        self.task_input = tk.Entry(root, font=("Arial", 12), width=30)
        self.task_input.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", font=("Arial", 12), command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_list_label = tk.Label(root, text="Your Tasks:", font=("Arial", 12))
        self.task_list_label.pack(pady=5)

        self.task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=15)
        self.task_listbox.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Completed", font=("Arial", 12), command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", font=("Arial", 12), command=self.update_task)
        self.update_button.pack(pady=5)

    def add_task(self):
        """
        Adds a new task to the to-do list.
        """
        task = self.task_input.get().strip()
        if not task:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")
            return

        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {"description": task, "completed": False}
        self.update_task_listbox()
        self.task_input.delete(0, tk.END)

    def update_task_listbox(self):
        """
        Updates the Listbox widget with the current tasks.
        """
        self.task_listbox.delete(0, tk.END)
        for task_id, details in self.tasks.items():
            status = "✓" if details["completed"] else "✗"
            self.task_listbox.insert(tk.END, f"[{task_id}] {details['description']} ({status})")

    def mark_completed(self):
        """
        Marks the selected task as completed.
        """
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")
            return

        task_id = int(self.task_listbox.get(selected[0]).split("]")[0][1:])
        self.tasks[task_id]["completed"] = True
        self.update_task_listbox()

    def delete_task(self):
        """
        Deletes the selected task from the to-do list.
        """
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
            return

        task_id = int(self.task_listbox.get(selected[0]).split("]")[0][1:])
        del self.tasks[task_id]
        self.update_task_listbox()

    def update_task(self):
        """
        Updates the description of the selected task.
        """
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
            return

        task_id = int(self.task_listbox.get(selected[0]).split("]")[0][1:])
        new_description = self.task_input.get().strip()
        if not new_description:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")
            return

        self.tasks[task_id]["description"] = new_description
        self.update_task_listbox()
        self.task_input.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
