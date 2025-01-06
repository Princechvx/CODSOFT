import tkinter as tk
from tkinter import messagebox
import json
import os


class ToDoListApp:
    def __init__(self, root):
        """
        Initializes the To-Do List application with data persistence.
        """
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")
        self.file_path = "todo_list_data.json"

        # Load tasks from file
        self.tasks = {}
        self.load_data()

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
        self.update_task_listbox()

        self.complete_button = tk.Button(root, text="Mark as Completed", font=("Arial", 12), command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset All Tasks", font=("Arial", 12), command=self.reset_tasks)
        self.reset_button.pack(pady=5)

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
        self.save_data()
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
        self.save_data()
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
        self.save_data()
        self.update_task_listbox()

    def reset_tasks(self):
        """
        Resets all tasks and optionally deletes saved data.
        """
        confirm = messagebox.askyesno("Reset Tasks", "Do you want to reset all tasks and delete saved data?")
        if confirm:
            self.tasks = {}
            if os.path.exists(self.file_path):
                os.remove(self.file_path)
            self.update_task_listbox()
            messagebox.showinfo("Tasks Reset", "All tasks and saved data have been reset.")

    def save_data(self):
        """
        Saves the current tasks to a JSON file.
        """
        with open(self.file_path, "w") as file:
            json.dump(self.tasks, file)

    def load_data(self):
        """
        Loads the tasks from a JSON file if it exists.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.tasks = json.load(file)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
