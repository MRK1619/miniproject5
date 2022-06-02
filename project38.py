# Weight Converter
from tkinter import *
# Creating A GUI Window
window = Tk()
def from_kg():
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    t1.delete("1.0",END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
e1 = Label(window, text="Input the weight in KG")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Gram")
e4 = Label(window, text="Pound")
t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
b1 = Button(window, text="Convert", command=from_kg)
e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
b1.grid(row=0, column=2)
window.mainloop()