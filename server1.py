import socket
import os
import subprocess

s = socket.socket()
ip="192.168.43.202"
port=1114
s.bind( (ip,port) )
s.listen()

client_session , client_address = s.accept()


while True:
	data = client_session.recv(20)
	choise = data.decode()
	if int(choise)==1:
		output = subprocess.getoutput("date")
		print(output)
		output = output.encode()
		client_session.send(output)
	elif int(choise)==2:
		output = subprocess.getoutput("cal")
		print(output)
		output = output.encode()
		client_session.send(output)
	elif int(choise)==3:
		output = subprocess.getoutput("bc")
		print(output)
		output = output.encode()
		client_session.send(output)
	elif int(choise)==4:
		output = subprocess.getoutput("exit")
		print(output)
	elif int(choise)==5:
		output = subprocess.getoutput("python36 capture.py")
