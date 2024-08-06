import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("More on the window")
window_width = 600
window_height = 400
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()
left = int(display_width/2 - window_width/2)
top = int(display_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')
window.iconbitmap('TwitterX.ico')

# window sizes
window.minsize(300,200)
#window.maxsize(800,500)
window.resizable(True, True)

# screen attributes
print(f"Resolution: {window.winfo_screenwidth()} x {window.winfo_screenheight()}")

# windown attributes
window.attributes('-alpha', 1) #transparent
window.attributes('-topmost', False) # alsway on top
window.attributes('-disable', False) # disable window
window.attributes('-fullscreen', False) # fullscreen

# title bar
window.overrideredirect(True) #hide title bar
resize = ttk.Sizegrip(window)
resize.place(relx=1.0, rely=1.0, anchor='se')
 
#security event
window.bind('<Alt-F4>', lambda event: window.quit())

# run
window.mainloop()