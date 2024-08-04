import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title("Frame and parent")

# frame
frame = ttk.Frame(window,
                 height=100,
                 width=200,
                 borderwidth=10,
                 relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side='left')

# master setting(parenting)
label = ttk.Label(frame, text='Label in frame')
label.pack()
button = ttk.Button(frame, text='Button in frame')
button.pack()

label2 = ttk.Label(window, text='Label out frame')
label2.pack(side='right')

# run
window.mainloop()