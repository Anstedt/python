import os
import subprocess

from tkinter import *
import tkinter as tk
from tkinter import ttk

class DiskSpeed:
  disks = []
    
  def __init__(self):
    self.root = Tk()
    self.get_disks()
    self.get_disk_info()
    self.parse_disk_info()
    self.display_disk_info()

  def my_print(self, event):
    print(self.value_list[0])
    # l1r.config(text = str(self.value_list[0]))
    l1r_text.set(self.disks[self.disk_letters.current()])
    l2r.config(text = str(self.value_list[1]))
    l3r.config(text = str(self.value_list[2]))

    # Update Combo box
    self.combo_text.set(self.disks[self.disk_letters.current()])
    
    # global disk_ltr
    # disk_ltr = tk.StringVar()
    # disk_ltr.set(self.disks[self.disk_letters.current()])
    # # entry = "Letter"+disk_ltr+"HOWARD"
    # l1r_text.set(disk_ltr.get())
    # print(l1r_text.get())
    # l2r_text = "NEW"
    # l3r_text = "OLD"
    # print(disk_ltr)
    # l1r.config(textvariable = l1r_text)
    # l2r.config(textvariable = l2r_text)
    # l3r.config(text = "WOW")
    # print("You Select" , self.disks[self.disk_letters.current()], "This Letter", event)
    
  def get_disks(self):
    print("Start Disk Letters")
    drives_cmd = "wmic logicaldisk get name > drive_letters.log"
    os.system(drives_cmd)
    
    # Now read the file and process it
    file = open("drive_letters.log", 'rt')
    lines = file.read().splitlines()
    file.close()

    x = 0
    for line in lines:
      index = line.find(":")
      if (index != -1):
        print("line=", line, "x=", x, "line02=", (line[1:2]))
        self.disks.insert(x, (line[1:2]))
        print(self.disks[x])
        x += 1

    #self.disk_name = tk.StringVar(value = self.disks[0])
    # print(self.disks[0], self.disk_name.get())
    ###disk_letters = ttk.Combobox(self.root, textvariable = self.disk_name)
    self.combo_text = StringVar()
    self.combo_text.set("Select Disk Letter")
    self.disk_letters = ttk.Combobox(self.root, textvariable=self.combo_text, values = self.disks)

    # self.disk_letters.configure(values = self.disks)
    ### self.disk_letters.grid(column = 0, row = 0)
    self.disk_letters.grid()
    # disk_letters.bind('<<ComboboxSelected>>', self.my_print)
    ### disk_letters.bind('<<ComboboxSelected>>', lambda even: print(self.disk_name.get()))
    self.disk_letters.bind('<<ComboboxSelected>>', self.my_print)

    
  def get_disk_info(self):
    print("Start Disk Speed")
    # Disk Speed
    dsk_drv = "C"

    logf="disk_"+dsk_drv+"_info.log"

    # Get Disk Info
    ### result = subprocess.run(["winsat" , "disk" , "-drive", "C"], shell=True, capture_output=True, text=True)
    ### print("Result:", result.stdout, file=open(logf, 'w'))

    # Now read the file and process it
    file = open(logf, 'rt')

    self.lines = file.read().splitlines()
    file.close()

  def parse_disk_info(self):
    list_index = 0
    self.title_list = list(("A", "B", "C"))
    self.value_list = list(("A", "B", "C"))
    self.units_list = list(("A", "B", "C"))

    for line in self.lines:
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
        self.title_list[list_index] = line[index:title_index]
        self.value_list[list_index] = float(result[:result.find(" ")])
        self.units_list[list_index] = result[result.find(" "):]
        list_index = list_index + 1
        
  def display_disk_info(self):
    ttk.Entry(self.root).grid(column = 1, row = 0)

    # Title
    lp = ttk.Label(self.root, text="Title", font="helvetica 24", width=19)
    lp.grid(padx=0, pady=0)
    lp.grid(column = 0, row = 1)

    # Disk Info
    l1 = ttk.Label(self.root, text=self.title_list[0], font="helvetica 16", width=28)
    l1.grid(padx=1, pady=0)
    l1.grid(column = 0, row = 2)

    global l1r_text, l1r
    l1r_text = StringVar()
    l1r_text.set("TEST")
    l1r = ttk.Label(self.root, textvariable=l1r_text, font="helvetica 16", width=28)
    l1r.grid(padx=1, pady=0)
    l1r.grid(column = 1, row = 2)
    
    # Disk Info
    l2 = ttk.Label(self.root, text=self.title_list[1], font="helvetica 16", width=28)
    l2.grid(padx=1, pady=0)
    l2.grid(column = 0, row = 3)

    global l2r
    l2r = ttk.Label(self.root, text="two", font="helvetica 16", width=28)
    l2r.grid(padx=1, pady=0)
    l2r.grid(column = 1, row = 3)

    # Disk Info
    l3 = ttk.Label(self.root, text=self.title_list[2], font="helvetica 16", width=28)
    l3.grid(padx=1, pady=0)
    l3.grid(column = 0, row = 4)

    global l3r
    l3r = ttk.Label(self.root, text="three", font="helvetica 16", width=28)
    l3r.grid(padx=1, pady=0)
    l3r.grid(column = 1, row = 4)

def main():
  ds = DiskSpeed();
  ds.root.mainloop()

if __name__ == '__main__':
  main()


      # def font_changed(font):
#     l['font'] = font

# root.tk.call('tk', 'fontchooser', 'configure', '-font', 'helvetica 24', '-command', root.register(font_changed))
# root.tk.call('tk', 'fontchooser', 'show')


