import tkinter as tk
from tkinter import ttk

def get_pos(event):
    pass

# setup
window = tk.Tk()
window.title('Combo and Spin')
window.geometry('600x400')

# combobox
items = ('Ice cream', 'Pizza', 'Nachos')
food_str = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_str)
combo['value'] = items # combo.configure(values = items)
combo.pack()

# events combobox
combo.bind('<<ComboboxSelected>>', lambda event: print(food_str.get()))

# spin edit
spin_int = tk.IntVar(value=1)
spin = ttk.Spinbox(window, textvariable=spin_int, from_=1, to=5, increment=0.5, command=lambda: print(spin_int.get())) 
#spin['value'] = (1,2,3,4,5)
spin.bind('<<Increment>>', lambda event: print('UP'))
spin.bind('<<Decrement>>', lambda event: print('DOWN'))
spin.pack()

# run
window.mainloop()