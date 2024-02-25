import os

dsk_drv = "C"

logf="hja"+dsk_drv+".log"

cmd = "winsat disk -drive C > " + logf
#print(cmd)

#ret = os.system(cmd)
#print(ret)

file = open(logf, 'rt')

lines = file.read().splitlines()
file.close()
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
    title = line[index:title_index]
    value = float(result[:result.find(" ")])
    units = result[result.find(" "):]
    print("title=", title, "result=", result, "value=", value, "units=", units)

# while file:
# print(file.read(),end="")


# Disk  Random 16.0 Read                       2169.84 MB/s          9.3
# Disk  Sequential 64.0 Read                   6951.92 MB/s          9.9
# Disk  Sequential 64.0 Write                  5411.91 MB/s          9.7
# Average Read Time with Sequential Writes     0.040 ms          8.9
# Latency: 95th Percentile                     0.097 ms          8.9
# Latency: Maximum                             1.002 ms          8.9
