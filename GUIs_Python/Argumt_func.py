import tkinter as tk
from tkinter import ttk

def button_func(string):
    def inner_func():
        print('A button was pressed')
        print(string.get())
    return inner_func

# setup
window = tk.Tk()
window.title("Button, function and argument")

#widgets
entry_string = tk.StringVar(value='Test')
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text='Button', command=button_func(entry_string))
button.pack()

# run
window.mainloop()

# to implement function button with argument, there are 2 way:
    #1. insert lambda function
        # ex : button = ttk.Button(window, text='Button', command= lambda : button_func(entry_string))
    #2. define inner function and need to return inner function