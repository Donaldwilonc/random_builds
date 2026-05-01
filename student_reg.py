import tkinter

students_list = []

def add_students(): 
    register = entry1.get()
    if len(students_list) < 34:
        if register:
            entry1.delete(0, tkinter.END)
            students_list.append(register)
    if len(students_list) == 34:
        btn1.config(state="disabled")

def close_window():
    exit()        
def open_new_window():
    win2 = tkinter.Toplevel(win)
    win2.title("Registered Students")
    win2.geometry("400x300")
    list1 = tkinter.Label(win2, text = "Registered students")
    list1.grid(row=3, column=0, padx=5)
    listbox1 = tkinter.Listbox(win2, width=40, height=10)
    listbox1.grid(row=4, column=0)
    for i, name in enumerate(students_list, start=1):
        listbox1.insert(tkinter.END, f"{i}. {name}")
    
    
win = tkinter.Tk()
win.title("Student Registeration")
win.geometry("400x300")

name = tkinter.Label(win, text="Student Name:")
name.grid(row=0, column=0, padx=1, pady=1)

entry1 = tkinter.Entry()
entry1.grid(row=0, column=1)

btn1 = tkinter.Button(win, text = "Add", fg = "black", bg = "yellow", command=add_students)
btn1.grid(row = 2, column = 1)

btn2 = tkinter.Button(win, text = "Open List", fg = "black", bg = "yellow", command=open_new_window)
btn2.grid(row = 2, column = 2)

btn4 = tkinter.Button(win, text="Exit", fg="red", bg="white", command=close_window)
btn4.place(x=170, y=100)

tkinter.mainloop()
