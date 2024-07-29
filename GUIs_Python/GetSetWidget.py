import tkinter as tk
from tkinter import ttk

# function
def btn_function():
    # get the content of the entry
    entry_text = entry.get()
    # update the label
    #label.config(text=entry_text)       #way1
    #label.configure(text=entry_text)    #way2
    label['text'] = entry_text           #way3
    # entry state
    entry['state'] = 'disabled'

def reset_btn():
    # reset lable
    label['text'] = 'Some text'
    # reset entry state
    entry['state'] = 'enabled'

# window
window = tk.Tk()
window.title("Getting and Setting widget")

# widget
label = ttk.Label(master=window, text='Some text')
label.pack()
entry = ttk.Entry(master=window)
entry.pack()
button = ttk.Button(master=window, text='The button', command=btn_function)
button.pack()
reset_button = ttk.Button(master=window, text='Reset', command=reset_btn)
reset_button.pack()

# run
window.mainloop()