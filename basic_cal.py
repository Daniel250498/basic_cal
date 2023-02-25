import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.create_widgets()

    def create_widgets(self):
        self.num1_label = tk.Label(self.master, text="Enter first number:")
        self.num1_label.grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = tk.Entry(self.master)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.num2_label = tk.Label(self.master, text="Enter second number:")
        self.num2_label.grid(row=1, column=0, padx=5, pady=5)
        self.num2_entry = tk.Entry(self.master)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.master, text="+", command=self.add)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)

        self.subtract_button = tk.Button(self.master, text="-", command=self.subtract)
        self.subtract_button.grid(row=2, column=1, padx=5, pady=5)

        self.multiply_button = tk.Button(self.master, text="*", command=self.multiply)
        self.multiply_button.grid(row=3, column=0, padx=5, pady=5)

        self.divide_button = tk.Button(self.master, text="/", command=self.divide)
        self.divide_button.grid(row=3, column=1, padx=5, pady=5)

        self.result_label = tk.Label(self.master, text="Result:")
        self.result_label.grid(row=4, column=0, padx=5, pady=5)
        self.result_entry = tk.Entry(self.master)
        self.result_entry.grid(row=4, column=1, padx=5, pady=5)

    def add(self):
        num1 = float(self.num1_entry.get())
        num2 = float(self.num2_entry.get())
        result = num1 + num2
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)

    def subtract(self):
        num1 = float(self.num1_entry.get())
        num2 = float(self.num2_entry.get())
        result = num1 - num2
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)

    def multiply(self):
        num1 = float(self.num1_entry.get())
        num2 = float(self.num2_entry.get())
        result = num1 * num2
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)

    def divide(self):
        num1 = float(self.num1_entry.get())
        num2 = float(self.num2_entry.get())
        result = num1 / num2
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()