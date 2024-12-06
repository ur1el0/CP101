#Roosc Zano

import tkinter
from tkinter import *


def Addition():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    ans["text"] = num1 + num2
def Subtract():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    ans["text"] = num1 - num2


def Multiplication():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    ans["text"] = num1 * num2


def Division():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    ans["text"] = num1 / num2


def ModulusDivFunction():
    num1 = float(first_num.get())
    num2 = float(sec_num.get())
    ans["text"] = num1 % num2


ros = tkinter.Tk()
ros.title("Calculator")
ros.geometry("550x200")

bel1 = Label(ros, text="1st number: ")
bel1.config(bg='#CDE8E5')
bel1.place(x=10, y=20)

first_num = Entry(ros)
first_num.place(x=120, y=20)

bel2 = Label(ros, text="2nd number: ")
bel2.config(bg='#CA8787')
bel2.place(x=10, y=70)

sec_num = Entry(ros)
sec_num.place(x=120, y=70)

plus = Button(ros, text="Addition", command=Addition)
plus.config(bg="grey")
plus.place(x=3, y=120)

minus = Button(ros, text="Subtraction", command=Subtract)
minus.config(bg="grey")
minus.place(x=75, y=120)

times = Button(ros, text="Multiplication", command=Multiplication)
times.config(bg="grey")
times.place(x=172, y=120)

divide = Button(ros, text="Division", command=Division)
divide.config(bg="grey")
divide.place(x=280, y=120)

mod = Button(ros, text="Modulus Division Function", command=ModulusDivFunction)
mod.config(bg="grey")
mod.place(x=355, y=120)

ans = Label(ros, text="Answer: ")
ans.place(x=10, y=170)


ros.config(bg="pink")
ros.mainloop()