import os
print("datanode setup is running")
print("enter ip")
remote_ip = input()
os.system("ssh {} iptables -F".format(remote_ip))
print("firewall temporary off")
os.system("ssh {} hostnamectl set-hostname dn2.lw.com".format(remote_ip))
print("hostname change")
os.system("ssh -X {} gedit /etc/hosts".format(remote_ip))
print("edit cmplte")
os.system("ssh {} mkdir -p etc/hadoop/data".format(remote_ip))
print("directory created")
os.system("scp /root/Desktop/myproject/datanode/core-site.xml {}:/etc/hadoop/".format(remote_ip))
print("file sent core")
os.system("scp /root/Desktop/myproject/datanode/hdfs-site.xml {}:/etc/hadoop/".format(remote_ip))
print("file sent hdfs")
os.system("ssh {} hadoop-daemon.sh start datanode".format(remote_ip))
print("start service")
print("datanode setup is ready")

