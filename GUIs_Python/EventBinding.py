import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'x: {event.x} y: {event.y}')

# setup
window = tk.Tk()
window.title('Event Binding')
window.geometry('600x500')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='Button')
button.pack()

# events
button.bind('<Alt-a>', lambda event: print(event))
text.bind('<Motion>', get_pos)
window.bind('<KeyPress>', lambda event: print(f'{event.char} was pressed'))
entry.bind('<FocusIn>', lambda event: print('Entry field is selected'))
entry.bind('<FocusOut>', lambda event: print('Entry field is not selected'))

# run
window.mainloop()

# Read more : https://www.pythontutorial.net/tkinter/tkinter-event-binding/