import os

logf="hja2.log"

cmd=[]
cmd.append("winsat disk -drive C > ")
cmd.append(logf)

# Convert list to string
cov_str = map(str, cmd)
cmd_str = "".join(cov_str)

ret = os.system(cmd_str)
#ret = os.system('winsat disk -drive C > logf')
print(ret)

file = open(logf, 'rt')
print(file.read(),end="")
