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
    # self.get_disk_info()
    self.button_control()
    # self.parse_disk_info()
    # self.display_disk_info()

  def my_print(self, event):
    # print(self.value_list[0])
    l1r.config(text = str(self.value_list[0]))
    # This works but not neede here: l1r_text.set(self.disks[self.disk_letters.current()])
    l2r.config(text = str(self.value_list[1]))
    l3r.config(text = str(self.value_list[2]))

    # Update Combo box
    self.combo_text.set(self.disks[self.disk_letters.current()])

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
        # print("line=", line, "x=", x, "line02=", (line[1:2]))
        self.disks.insert(x, (line[1:2]))
        # print(self.disks[x])
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

    
  def getdiskinfo(self):
    print("Button", self.disks[self.disk_letters.current()])
    self.get_disk_info()
    self.parse_disk_info()
    self.display_disk_info()
    
  def button_control(self):
    button = Button(self.root, text="HJA", command=self.getdiskinfo)
    button.grid(column = 2, row = 0)



    
  def get_disk_info(self):
    print("Start Disk Speed")
    # Disk Speed
    dsk_drv = self.disks[self.disk_letters.current()]
    print("Disk Drive=", dsk_drv)

    logf="disk_"+dsk_drv+"_info.log"

    # Get Disk Info, debug
    result = subprocess.run(["winsat" , "disk" , "-drive", dsk_drv], shell=True, capture_output=True, text=True)
    print("Result:", result.stdout, file=open(logf, 'w'))

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
        self.title_list[list_index] = line[index:title_index].strip()
        self.value_list[list_index] = f"{float(result[:result.find(" ")]):.2f}"
        self.units_list[list_index] = result[result.find(" "):].strip()
        list_index = list_index + 1

  def display_disk_info(self):
    # estyle = ttk.Style()
    # estyle.element_create("plain.field", "from", "clam")
    # estyle.layout("EntryStyle.TEntry", [('Entry.plain.field', {'children': [('Entry.background', {'children': [('Entry.padding', {'children': [('Entry.textarea', {'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})], 'border':'2', 'sticky': 'nswe'})])
    # estyle.configure("EntryStyle.TEntry", background="green", foreground="grey", fieldbackground="blue")
    # ttk.Entry(self.root, style="EntryStyle.TEntry").grid(column = 1, row = 0)
    estyle = ttk.Style()
    estyle.configure('style.TEntry', fieldbackground="red", foreground="orange")
    ttk.Entry(self.root, style='style.TEntry').grid(column = 1, row = 0)

    # Heading
    lp = ttk.Label(self.root, text="Title", font="helvetica 24", width=12, borderwidth=2, relief="raised")
    lp.grid(padx=0, pady=0)
    lp.grid(column = 0, row = 1)

    # Disk Info 1
    global l1r_text, l1r
    global l1v_text, l1v
    (l1r_text, l1r, l1v_text, l1v) = self.create_disk_info(0, 0, 2)

    # Disk Info 2
    global l2r_text, l2r
    global l2v_text, l2v
    (l2r_text, l2r, l2v_text, l2v) = self.create_disk_info(1, 0, 3)

    # Disk Info 3
    global l3r_text, l3r
    global l3v_text, l3v
    (l3r_text, l3r, l3v_text, l3v) = self.create_disk_info(2, 0, 4)

  def create_disk_info(self, index, col, row_num):
    # "flat", "raised", "sunken", "ridge", "solid", and "groove".
    lb = ttk.Label(self.root, text=self.title_list[index], font="helvetica 16", width=22, borderwidth=2, relief="raised")
    lb.grid(padx=1, pady=0)
    lb.grid(column = col, row = row_num)

    lbr_text = StringVar()
    lbr_text.set(self.value_list[index])
    lbr = ttk.Label(self.root, textvariable=lbr_text, font="helvetica 16", width=10, borderwidth=4, relief="raised", anchor="e")
    lbr.grid(padx=1, pady=0)
    lbr.grid(column = (col+1), row = row_num)

    lbv_text = StringVar()
    lbv_text.set(self.units_list[index])
    lbv = ttk.Label(self.root, textvariable=lbv_text, font="helvetica 16", width=6, borderwidth=4, relief="raised", anchor="center")
    lbv.grid(padx=1, pady=0)
    lbv.grid(column = (col+2), row = row_num)

    return(lbr_text, lbr, lbv_text, lbv) 
        
def main():
  ds = DiskSpeed();
  ds.root.mainloop()

if __name__ == '__main__':
  main()


# def font_changed(font):
#     l['font'] = font

# root.tk.call('tk', 'fontchooser', 'configure', '-font', 'helvetica 24', '-command', root.register(font_changed))
# root.tk.call('tk', 'fontchooser', 'show')


