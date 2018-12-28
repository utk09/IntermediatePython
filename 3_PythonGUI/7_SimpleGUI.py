from tkinter import * # tkinter is default  GUI Library in Python
import random

window = Tk() # create window contents as children to "window"
my_label = Label(window, text="Random Number [1, 20]").pack()
my_label_n = Label(window, text=" ")
my_label_n.pack()


def clicked():
    my_label_n.configure(text=random.randint(1, 20))


btn = Button(window, text="Generate", command=clicked).pack()

window.mainloop()
