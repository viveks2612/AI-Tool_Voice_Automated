import os
import subprocess
ch = input()
if int(ch)==1:
	output = subprocess.getoutput("python36 capture.py")
	print(output)
elif int(ch)==2:
	output = subprocess.getoutput("cal")
	print(output)
