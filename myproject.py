import os
os.system("echo welcome to AI project | festival --tts")
print("\t\t\tAI PROJECT")
print("\t\t\t..........")


print("Do you want to run the program on local system or remote system")
os.system("tput setaf 4")
print("1.Type local for local system")
print("2.Type remote for remote system")
os.system("tput setaf 0")

location = input()
print(location)

if location=="local":
	os.system("echo local | festival --tts")
	print(""" 1. press 1 to show date
 2. press 2 to show camera
 3. press 3 to show calender
 4. press 4 to exit""")
	print("enter choise")
	ch = input()
	print(ch)
	if int(ch)==1:
		os.system("date")
	elif int(ch)==2:
		os.system("python36 capture.py")
	elif int(ch)==3:
		os.system("cal")
	elif int(ch)==4:
		exit()
	else:
		print("wrong option")

elif location == "remote":
	os.system("echo remote | festival --tts")
	print(""" 1. press 1 to show date
 2. press 2 to show camera
 3. press 3 to show calender
 4. press 4 to exit""")	
	print("enter Internet protocol")
	remote_ip = input()
	print("enter choise")
	ch = input()
	print(ch)
	if int(ch)==1:
		os.system("ssh {} date".format(remote_ip))
	elif int(ch)==2:
		os.system("scp capture.py {}:/root/Desktop".format(remote_ip))
		os.system("ssh {} python36 /root/Desktop/capture.py".format(remote_ip))
		os.system("scp {}:/root/Desktop/vivek.png /root/Desktop/myproject".format(remote_ip))	
	elif int(ch)==3:
		os.system("ssh {} cal".format(remote_ip))
	elif int(ch)==4:
		exit()
	else:
		print("wrong option")
else:
	print("you did not choose local or remote")
