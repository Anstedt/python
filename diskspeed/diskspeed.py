import os

from tkinter import *
from tkinter import ttk

dsk_drv = "C"

logf="hja"+dsk_drv+".log"

# This gets the disk speed aand saves it to a file
cmd = "winsat disk -drive C > " + logf
# os.system(cmd)

# Now read the file and process it
file = open(logf, 'rt')

lines = file.read().splitlines()
file.close()

list_index = 0
title_list = list(("A", "B", "C"))
value_list = list(("A", "B", "C"))
units_list = list(("A", "B", "C"))

for line in lines:
  index = line.find("Disk")
  if (index != -1):
    # Find the index to the end of the title by looking for trailing spaces
    title_index = line.find("   ")
    # The result is from the end of the title to the end of the string, and get rid of leading and trailing spaces
    result = line[title_index:].strip()
    # Now find the end of the result so we can get the value and units but not the trailing numbers
    result_index = result.find("   ")
    # This is the result and the units
    result = result[:result_index]

    # Now pick up the pieces we want
    title_list[list_index] = line[index:title_index]
    value_list[list_index] = float(result[:result.find(" ")])
    units_list[list_index] = result[result.find(" "):]
    list_index = list_index + 1
    # print("title=", title, "result=", result, "value=", value, "units=", units)
    print(len(title_list))
    print(title_list)

root = Tk()
ttk.Entry(root).grid()

lp = ttk.Label(root, text="Title", font="helvetica 24", width=19)
lp.grid(padx=0, pady=0)

l1 = ttk.Label(root, text=title_list[0], font="helvetica 16", width=28)
l1.grid(padx=1, pady=0)

l2 = ttk.Label(root, text=title_list[1], font="helvetica 16", width=28)
l2.grid(padx=1, pady=0)

l3 = ttk.Label(root, text=title_list[2], font="helvetica 16", width=28)
l3.grid(padx=1, pady=0)

# def font_changed(font):
#     l['font'] = font

# root.tk.call('tk', 'fontchooser', 'configure', '-font', 'helvetica 24', '-command', root.register(font_changed))
# root.tk.call('tk', 'fontchooser', 'show')

root.mainloop()
