import subprocess

# result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)

result = subprocess.run(["winsat" , "disk" , "-drive", "C"], shell=True, capture_output=True, text=True)

print("Result:", result.stdout, file=open('log.log', 'a'))
