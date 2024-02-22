import subprocess
import os

command = "dir"
option = "/s"

args=[]
args.append(command)
args.append(option)
new_res = subprocess.call(args)

# result = subprocess.run('dir', stdout=subprocess.PIPE)

# ret = os.system('winsat disk -drive C > hja.log')
# print(ret)
# print(result.stderr)

#cmd = "date"

#returned_output = subprocess.check_output(cmd)

# using decode() function to convert byte string to string
#print('Current date is:', returned_output.decode("utf-8"))
