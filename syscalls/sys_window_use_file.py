import os

dsk_drv = "C"

logf="hja"+dsk_drv+".log"

cmd = "winsat disk -drive C > " + logf
#print(cmd)

ret = os.system(cmd)
#print(ret)

file = open(logf, 'rt')

lines = file.read().splitlines()
file.close()
for line in lines:
  index = line.find("Disk")
  if (index != -1):
    print(line[index:])
               
# while file:
# print(file.read(),end="")
