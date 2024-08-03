import tkinter as tk
from tkinter import ttk
from random import choice

# setup
window = tk.Tk()
window.geometry('600x400')
window.title("TreeView")

# data
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Link']
last_names = ['Smith', 'Hanna', 'Wilson', 'Thomas', 'Cook', 'Taylor', 'Walker', 'Roxana', 'Clark']

# treeview
table = ttk.Treeview(window, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Surname',)
table.heading('email', text='Email',)
table.pack(fill='both', expand=True)

# insert value to table
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}{last}@gmail.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)

# insert to last row
table.insert(parent='', index=tk.END, values=('XXX', 'YYY', 'ZZZ'))

# event
def item_select(_):
    #print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', item_select)
table.bind('<Delete>', delete_items)

# run
window.mainloop()