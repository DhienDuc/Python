import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title("Menu")

# menu
menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command=lambda : print('New file'))
file_menu.add_command(label='Open', command=lambda : print('Open file'))
file_menu.add_separator()
menu.add_cascade(label='File', menu=file_menu)

# sub menu in sub menu
file_sub_menu = tk.Menu(menu, tearoff=False)
file_sub_menu.add_command(label='Save setting')
file_menu.add_cascade(label='Setting', menu=file_sub_menu)

# another sub menu
help_menu = tk.Menu(window, tearoff=False)
help_menu.add_command(label='Version', command=lambda : print('Version'))
help_check_str = tk.StringVar()
help_menu.add_checkbutton(label='Update', onvalue='on', offvalue='off', variable=help_check_str)
menu.add_cascade(label='Help', menu=help_menu)

# show menu on window
window.configure(menu=menu)

# menu button
menu_btn = ttk.Menubutton(window, text='Menu button')
menu_btn.pack()
btn_sub_menu = tk.Menu(menu_btn, tearoff=False)
btn_sub_menu.add_command(label='Entry1', command= lambda: print('Entry1'))
menu_btn.configure(menu=btn_sub_menu) # = menu_btn['menu'] = btn_sub_menu

# run
window.mainloop()

# https://www.tutorialspoint.com/python/tk_menu.htm