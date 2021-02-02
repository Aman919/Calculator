from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root, width=35,borderwidth=15)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) +str(number))


def button_clear():
    e.delete(0,END)

#define buttons

myButton_1 = Button(root, text="1",padx=40,pady=20,command=lambda: button_click(1))
myButton_2 = Button(root, text="2",padx=40,pady=20,command=lambda: button_click(2))
myButton_3 = Button(root, text="3",padx=40,pady=20,command=lambda: button_click(3))
myButton_4 = Button(root, text="4",padx=40,pady=20,command=lambda: button_click(4))
myButton_5 = Button(root, text="5",padx=40,pady=20,command=lambda: button_click(5))
myButton_6 = Button(root, text="6",padx=40,pady=20,command=lambda: button_click(6))
myButton_7 = Button(root, text="7",padx=40,pady=20,command=lambda: button_click(7))
myButton_8 = Button(root, text="8",padx=40,pady=20,command=lambda: button_click(8))
myButton_9 = Button(root, text="9",padx=40,pady=20,command=lambda: button_click(9))
myButton_0 = Button(root, text="0",padx=40,pady=20,command=lambda: button_click(0))

myButton_add = Button(root, text="+",padx=39,pady=20,command=button_click)

myButton_clear = Button(root, text="Clear",padx=79,pady=20,command=lambda: button_clear())
myButton_equals = Button(root, text="=",padx=91,pady=20,command=lambda: button_click())

#put buttons on the screen

myButton_1.grid(row=3,column=0)
myButton_2.grid(row=3,column=1)
myButton_3.grid(row=3,column=2)

myButton_4.grid(row=2,column=0)
myButton_5.grid(row=2,column=1)
myButton_6.grid(row=2,column=2)

myButton_7.grid(row=1,column=0)
myButton_8.grid(row=1,column=1)
myButton_9.grid(row=1,column=2)

myButton_0.grid(row=4,column=0)

myButton_add.grid(row=5,column=0)
myButton_clear.grid(row=4,column=1,columnspan=2)
myButton_equals.grid(row=5,column=1,columnspan=2)


root.mainloop()
