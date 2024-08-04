import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# setup
window = tk.Tk()
window.geometry('600x600')
window.title("Sliders")

# slider
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    window,
    command=lambda value: print(scale_float.get()),
    from_ = 0,
    to = 25,
    length=300,
    orient='horizontal',
    variable=scale_float)

scale.pack()

# progress bar
progress = ttk.Progressbar(
    window,
    variable=scale_float,
    maximum=25,
    orient='vertical',
    mode='indeterminate',
    length=100)
progress.pack()
#progress.start()

# Scrolledtext
scroll_text = scrolledtext.ScrolledText(window)
scroll_text.pack()

# exercise
exercise_int = tk.IntVar()
exercise_progress = ttk.Progressbar(window, variable=exercise_int)
exercise_progress.pack()
exercise_progress.start()
label = ttk.Label(window, textvariable=exercise_int)
label.pack()
exercise_scale = ttk.Scale(window, variable=exercise_int, from_=0, to=100)
exercise_scale.pack()

# run
window.mainloop()