import tkinter as tk
from tkinter import messagebox

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Homepage")

        self.label = tk.Label(root, text="Welcome to the Homepage", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.button1 = tk.Button(root, text="Page 1", command=self.open_page1)
        self.button1.pack()

        self.button2 = tk.Button(root, text="Page 2", command=self.open_page2)
        self.button2.pack()

        self.button3 = tk.Button(root, text="Page 3", command=self.open_page3)
        self.button3.pack()

    def open_page1(self):
        page1 = Page1(self.root)
        page1.show()

    def open_page2(self):
        page2 = Page2(self.root)
        page2.show()

    def open_page3(self):
        page3 = Page3(self.root)
        page3.show()

class Page1:
    def __init__(self, root):
        self.root = root
        self.root.title("Page 1")

        self.label = tk.Label(root, text="Page 1", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.name_label = tk.Label(root, text="Enter your name:")
        self.name_label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_name)
        self.submit_button.pack()

    def submit_name(self):
        name = self.name_entry.get()
        if name:
            self.root.destroy()
            page2 = Page2(self.root, name)
            page2.show()
        else:
            messagebox.showwarning("Warning", "Please enter your name.")

class Page2:
    def __init__(self, root, name=""):
        self.root = root
        self.root.title("Page 2")

        self.label = tk.Label(root, text="Page 2", font=("Helvetica", 16))
        self.label.pack(pady=20)

        if name:
            greeting_label = tk.Label(root, text=f"Hello, {name}!")
            greeting_label.pack()
        else:
            warning_label = tk.Label(root, text="Name not entered.")
            warning_label.pack()

class Page3:
    def __init__(self, root):
        self.root = root
        self.root.title("Page 3")

        self.label = tk.Label(root, text="Page 3", font=("Helvetica", 16))
        self.label.pack(pady=20)

def main():
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
