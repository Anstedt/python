import subprocess

# Define command and options wanted
command = "head"
options = "-n 1"
# Ask user for file name(s) - now it's safe from shell injection
filename = input("Please introduce name(s) of file(s) of interest:\n")
# Create list with arguments for subprocess.call
args=[]
args.append(command)
args.append(options)
for i in filename.split():
    args.append(i)
# Run subprocess.call and save return_value
return_value = subprocess.call(args)
print('###############')
print('Return value:', return_value)
