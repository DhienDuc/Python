import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title("Tabs")

# notebook
notebook = ttk.Notebook(window)
# tab 1
tab1 = ttk.Frame(notebook)
lable1 = ttk.Label(tab1, text='Label in tab 1')
lable1.pack()
button1 = ttk.Button(tab1, text='Button in tab 1')
button1.pack()
# tab 2
tab2 = ttk.Frame(notebook)
lable2 = ttk.Label(tab2, text='Label in tab 2')
lable2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.pack()

# run
window.mainloop()