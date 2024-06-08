from ipaddress import *
kol = 0
net = ip_network("192.168.248.176/255.255.255.240", False)
for ip in net.hosts():
    s = str(ip)
    m = s.split('.')
    print(m)
    j = ''
    for i in m:
        j = j.join(bin(int(i))[::2])

    print(j.count('1'), j.count('0'))
print(kol)