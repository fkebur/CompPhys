#!/usr/bin/env python

from tkinter import *
import sys

def hello():
    print("Hello, world!")

def goodbye():
    print("Goodbye, cruel world!")
    sys.exit(0)

root = Tk()
frame = Frame(root)
b1 = Button(frame, text="Hello", width=15, command=hello).pack()
b2 = Button(frame, text="Goodbye", width=15, command=goodbye).pack()
frame.pack()
mainloop()
