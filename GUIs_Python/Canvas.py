import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title("Canvas")

# canvas
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/create_rectangle.html
canvas = tk.Canvas(window, bg='gray')
canvas.pack()

canvas.create_rectangle((50, 20, 100, 200), fill='red', width='5', outline='green')
canvas.create_line((0, 0, 100, 150), fill='white')
canvas.create_oval((200, 0, 300, 100), fill='pink')
canvas.create_arc((200, 0, 300, 100), fill='yellow', start = 0, extent = -90, style = tk.ARC, outline = "purple", width = '8')
canvas.create_arc((200, 0, 300, 100), fill='yellow', start = 90, extent = 90)
canvas.create_polygon((120, 80, 100, 150, 180, 50), fill='blue')

canvas.create_text((100, 200), text='this is text', fill='orange', width=40)
canvas.create_window((50, 100), window=ttk.Button(window, text='Button'))

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x-size/2, y-size/2, x+size/2, y+size/2), fill='black')

def size_adjust(event):
    global size
    if event.delta > 0:
        size += 2
    else:
        if size > 2:
            size -= 2
        else:
            size = 2
    size = max(0, min(size, 20))

size = 2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', size_adjust)

# run
window.mainloop()