from tkinter import *

window = Tk()


def convert():
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    t3.delete('1.0', END)
    try:
        to_grams = float(e1_val.get()) * 1000
        to_pounds = float(e1_val.get()) * 2.20462
        to_ounces = float(e1_val.get()) * 35.274
        t1.insert(END, to_grams)
        t2.insert(END, to_pounds)
        t3.insert(END, to_ounces)
    except ValueError:
        t1.insert(END, "Cannot convert")
        t2.insert(END, "Cannot convert")
        t3.insert(END, "Cannot convert")


t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)
t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)
t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

b1 = Button(window, text="Convert", command=convert)
b1.grid(row=0, column=2)

e1_val = StringVar()
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)

l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)


window.mainloop()
