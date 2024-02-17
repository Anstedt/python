from tkinter import *
from tkinter import ttk

root = Tk()
ttk.Entry(root).grid()

l = ttk.Label(root, text="Hello World", font="helvetica 24")
l.grid(padx=10, pady=10)

def font_changed(font):
    l['font'] = font

root.tk.call('tk', 'fontchooser', 'configure', '-font', 'helvetica 24', '-command', root.register(font_changed))
root.tk.call('tk', 'fontchooser', 'show')

root.mainloop()
