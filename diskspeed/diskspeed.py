import os

from tkinter import *
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
    print("You Select" , self.disks[self.disk_letters.current()], "This Letter", event)
    
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
        self.disks.insert(x, (line[0:2]))
        print(self.disks[x])
        x += 1

    #self.disk_name = tk.StringVar(value = self.disks[0])
    # print(self.disks[0], self.disk_name.get())
    ###disk_letters = ttk.Combobox(self.root, textvariable = self.disk_name)
    self.disk_letters = ttk.Combobox(self.root)

    
    self.disk_letters.configure(values = self.disks)
    self.disk_letters.grid()
    # disk_letters.bind('<<ComboboxSelected>>', self.my_print)
    ### disk_letters.bind('<<ComboboxSelected>>', lambda even: print(self.disk_name.get()))
    self.disk_letters.bind('<<ComboboxSelected>>', self.my_print)

    
  def get_disk_info(self):
    print("Start Disk Speed")
    # Disk Speed
    dsk_drv = "C"

    logf="hja"+dsk_drv+".log"

    # This gets the disk speed and saves it to a file
    cmd = "winsat disk -drive C > " + logf
    # os.system(cmd)

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
        # print("title=", title, "result=", result, "value=", value, "units=", units)
        # print(len(title_list))
        # print(title_list)

  def display_disk_info(self):
    ttk.Entry(self.root).grid()
    
    lp = ttk.Label(self.root, text="Title", font="helvetica 24", width=19)
    lp.grid(padx=0, pady=0)

    l1 = ttk.Label(self.root, text=self.title_list[0], font="helvetica 16", width=28)
    l1.grid(padx=1, pady=0)

    l2 = ttk.Label(self.root, text=self.title_list[1], font="helvetica 16", width=28)
    l2.grid(padx=1, pady=0)

    l3 = ttk.Label(self.root, text=self.title_list[2], font="helvetica 16", width=28)
    l3.grid(padx=1, pady=0)

def main():
  ds = DiskSpeed();
  ds.root.mainloop()

if __name__ == '__main__':
  main()


      # def font_changed(font):
#     l['font'] = font

# root.tk.call('tk', 'fontchooser', 'configure', '-font', 'helvetica 24', '-command', root.register(font_changed))
# root.tk.call('tk', 'fontchooser', 'show')


