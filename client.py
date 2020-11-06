import os
print("client setup is running..")
print("enter ip")
remote_ip = input()
os.system("ssh {} iptables -F".format(remote_ip))
print("firewall temporary off")
os.system("ssh {} hostnamectl set-hostname client.lw.com".format(remote_ip))
print("hostname change")
os.system("ssh -X {} gedit /etc/hosts".format(remote_ip))
print("edit cmplte")
os.system("ssh {} mkdir -p etc/hadoop/name".format(remote_ip))
print("directory created")
os.system("scp /root/Desktop/myproject/client/core-site.xml {}:/etc/hadoop/".format(remote_ip))
print("file sent core")
print("client setup is ready")


