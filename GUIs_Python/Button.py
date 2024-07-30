import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

# button
def btn_func():
    print(radio_var.get())

btn_string = tk.StringVar(value='button with stringvar')
# textvariable will overwrite text in ttk.Button() function
button = ttk.Button(window, text='A simple button', command=btn_func, textvariable=btn_string)
button.pack()

# check button
check_var = tk.IntVar(value=0) #value = 0(default : OFF), value = 1(default : ON)
check1 = ttk.Checkbutton(window, 
                        text='checkbox 1', 
                        command=lambda: print(check_var.get()), 
                        variable=check_var)
check1.pack()

check2 = ttk.Checkbutton(window, 
                        text='checkbox 2', 
                        command=lambda: check_var.set(0))
check2.pack()

# radio 
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, 
                         text='RadioButton 1', 
                         value='Radio 1',
                         variable=radio_var,
                         command=lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window,
                         text='RadioButton 2', 
                         value=2,
                         variable=radio_var)
radio2.pack()

# run
window.mainloop()