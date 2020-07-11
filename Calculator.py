from tkinter import *
root = Tk()
root.title('Calculator')

e = Entry(root,width=33, borderwidth=22)
e.grid(row=0, column=0, columnspan=4, padx=1, pady=10)

def button_click(number):
    #e.delete(0, END)
    #e.insert(0, number)
    current= e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    e.insert(0, str(current) - str(number))
    e.insert(0, str(current) * str(number))

def button_clear():
    e.delete(0, END)
def button_add():
    firest_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(firest_number)
    e.delete(0, END)

def button_subtract():
    firest_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(firest_number)
    e.delete(0, END)

def button_multi():
    firest_number = e.get()
    global f_num
    global math
    math = 'multi'
    f_num = int(firest_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multi':
        e.insert(0, f_num * int(second_number))

button_1 = Button(root, text='1', padx=30, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=30, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=30, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=30, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=30, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=30, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=30, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=30, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=30, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=30, pady=20, command=lambda: button_click(0))
button_add = Button(root, text='+', padx=29, pady=20, bg='orange', command=button_add)
button_subtract = Button(root, text='-', padx=30, pady=20, bg='orange',  command=button_subtract)
button_multi = Button(root, text='*', padx=30, pady=20, bg='orange',  command=button_multi)
button_equal = Button(root, text='=', padx=29, pady=20, bg='orange', command=button_equal)
button_clear = Button(root, text='Clear', padx=55, pady=20, command= button_clear)

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
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multi.grid(row=3, column=3)

button_equal.grid(row=4, column=3, columnspan=1)


root.mainloop()