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
    # s1 = line[index:]
    # Find the index to the end of the first string by looking for trailing spaces
    s2i = line.find("   ")
    s2 = line[s2i:]
    s2 = s2.strip()
    s3i = s2.find("   ")
    s2 = s2[:s3i]
    s1 = line[index:s2i]
    v2 = s2[:s2.find(" ")]
    u = s2[s2.find(" "):]
    # print(line[index:])
    print("s1=", s1, "s2=", s2, "v2=", v2, "u=", u)

# while file:
# print(file.read(),end="")


# Disk  Random 16.0 Read                       2169.84 MB/s          9.3
# Disk  Sequential 64.0 Read                   6951.92 MB/s          9.9
# Disk  Sequential 64.0 Write                  5411.91 MB/s          9.7
# Average Read Time with Sequential Writes     0.040 ms          8.9
# Latency: 95th Percentile                     0.097 ms          8.9
# Latency: Maximum                             1.002 ms          8.9
