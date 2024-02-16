import tkinter as tk
from tkinter import messagebox
from itertools import cycle

class GroupArrangerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Group Arranger App")

        self.names_label = tk.Label(master, text="Enter names (comma-separated):")
        self.names_label.pack()

        self.names_entry = tk.Entry(master, width=40)
        self.names_entry.pack()

        self.groups_label = tk.Label(master, text="Number of groups:")
        self.groups_label.pack()

        self.groups_entry = tk.Entry(master)
        self.groups_entry.pack()

        self.arrange_button = tk.Button(master, text="Arrange Groups", command=self.arrange_groups)
        self.arrange_button.pack()

    def arrange_groups(self):
        names_input = self.names_entry.get()
        num_groups_input = self.groups_entry.get()

        try:
            num_groups = int(num_groups_input)
            names = [name.strip() for name in names_input.split(',')]

            if len(names) == 0:
                messagebox.showwarning("Warning", "Please enter at least one name.")
                return

            if num_groups <= 0 or num_groups > len(names):
                messagebox.showwarning("Warning", "Invalid number of groups.")
                return

            grouped_names = {f"Group {i+1}": [] for i in range(num_groups)}
            cycle_groups = cycle(grouped_names.keys())

            for name in names:
                group = next(cycle_groups)
                grouped_names[group].append(name)

            result_message = "\n".join([f"{group}: {', '.join(names)}" for group, names in grouped_names.items()])
            messagebox.showinfo("Groups Arranged", result_message)

        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number of groups.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GroupArrangerApp(root)
    root.mainloop()
    