from tkinter import *

root = Tk()
root.title("SIMPLE CALCULATOR")
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

def add_button(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+ str(number))   #---> for two digit numbers

def addition():
    first_num = e.get()
    global num1
    global maths 
    maths = "addition"
    num1 = int(first_num)
    e.delete(0, END)

def substraction():
    first_num = e.get()
    global num1
    global maths 
    maths = "substraction"
    num1 = int(first_num)
    e.delete(0, END)

def multiply():
    first_num = e.get()
    global num1
    global maths 
    maths = "multiplication"
    num1 = int(first_num)
    e.delete(0, END)

def divide():
    first_num = e.get()
    global num1
    global maths 
    maths = "division"
    num1 = int(first_num)
    e.delete(0, END)

def equal():
    second_num = e.get()
    e.delete(0, END)
    if maths == "addition":
        e.insert(0, num1+int(second_num))
    if maths == "substraction":
        e.insert(0,num1 - int(second_num))
    if maths == "multiplication":
        e.insert(0, num1 * int(second_num))
    if maths == "division":
        e.insert(0, num1 / int(second_num))


def clear():
    e.delete(0, END)


#Creation of buttons ----->

button_1 = Button(root, text="1", padx=50, pady=20, command= lambda: add_button(1))
button_2 = Button(root, text="2", padx=50, pady=20, command= lambda: add_button(2))
button_3 = Button(root, text="3", padx=50, pady=20, command= lambda: add_button(3))
button_4 = Button(root, text="4", padx=50, pady=20, command= lambda: add_button(4))
button_5 = Button(root, text="5", padx=50, pady=20, command= lambda: add_button(5))
button_6 = Button(root, text="6", padx=50, pady=20, command= lambda: add_button(6))
button_7 = Button(root, text="7", padx=50, pady=20, command= lambda: add_button(7))
button_8 = Button(root, text="8", padx=50, pady=20, command= lambda: add_button(8))
button_9 = Button(root, text="9", padx=50, pady=20, command= lambda: add_button(9))
button_0 = Button(root, text="0", padx=50, pady=20, command= lambda: add_button(0))
button_add = Button(root, text="+", padx=40, pady=20, command= addition)
button_substract = Button(root, text="-", padx=40, pady=20, command= substraction)
button_multiplication = Button(root, text="*", padx=40, pady=20, command= multiply)
button_division = Button(root, text="/", padx=40, pady=20, command= divide)
button_equal = Button(root, text="=", padx=50, pady=20, command= equal)
button_clear = Button(root, text="<-", padx=50, pady=20, command= clear)


#positions of button ---->

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1)
button_clear.grid(row=4, column=2)

button_add.grid(row=1, column=4)
button_substract.grid(row=2, column=4)
button_multiplication.grid(row=3, column=4)
button_division.grid(row=4, column=4)

root.mainloop()