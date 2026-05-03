import tkinter as tk

win = tk.Tk()
win.title("App")
win.geometry("900x900")

# Definition group.
def get_numbers():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        return a, b
    except ValueError:
        result_label.config(text="Enter valid numbers!")
        return None, None

def add():
    a, b = get_numbers()
    if a is not None:
        result_label.config(text=f"Result: {a + b}")

def subtract():
    a, b = get_numbers()
    if a is not None:
        result_label.config(text=f"Result: {a - b}")

def multiply():
    a, b = get_numbers()
    if a is not None:
        result_label.config(text=f"Result: {a * b}")

def divide():
    a, b = get_numbers()
    if a is not None:
        if b == 0:
            result_label.config(text="Cannot divide by zero")
        else:
            result_label.config(text=f"Result: {a / b}")

# The first label and entry group.
label1 = tk.Label(win, text="First Number: ")
label1.grid(row=0, column=0)
entry1 = tk.Entry()
entry1.grid(row=0, column=1)

# The second label and entry group.
label2 = tk.Label(win, text="Second Number: ")
label2.grid(row=1, column=0)
entry2 = tk.Entry()
entry2.grid(row=1, column=1)

# The button group.
btn1 = tk.Button(win, text="Add", command=add)
btn1.grid(row=2, column=0)
btn2 = tk.Button(win, text="Subtract", command=subtract)
btn2.grid(row=2, column=1)
btn3 = tk.Button(win, text="Multiply", command=multiply)
btn3.grid(row=2, column=2)
btn4 = tk.Button(win, text="Divide", command=divide)
btn4.grid(row=2, column=3)

# Result side.
result_label = tk.Label(win, text="Result:")
result_label.grid(row=3, column=0, columnspan=4)

tk.mainloop()
