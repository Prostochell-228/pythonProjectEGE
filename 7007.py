from ipaddress import *
kol = 0
net = ip_network("117.32.0.0/255.224.0.0", False)
for ip in net.hosts():
    s = str(ip)
    m = s.split('.')
    if len(set(m))=="3.192.192.13.1":
        kol+=1
print(kol)