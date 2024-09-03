import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App")
        self.root.geometry("300x400")

        # Create a listbox to display todo items
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(padx=10, pady=10)

        # Create an entry field to input new todo items
        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10, pady=10)

        # Create buttons to add and remove todo items
        self.add_button = tk.Button(self.root, text="Add", command=self.add_todo)
        self.add_button.pack(padx=10, pady=10)

        self.remove_button = tk.Button(self.root, text="Remove", command=self.remove_todo)
        self.remove_button.pack(padx=10, pady=10)

    def add_todo(self):
        # Get the text from the entry field
        todo = self.entry.get()
        if todo:
            # Add the todo item to the listbox
            self.listbox.insert(tk.END, todo)
            # Clear the entry field
            self.entry.delete(0, tk.END)

    def remove_todo(self):
        # Get the selected todo item from the listbox
        try:
            todo_index = self.listbox.curselection()[0]
            self.listbox.delete(todo_index)
        except IndexError:
            messagebox.showerror("Error", "Select a todo item to remove")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()