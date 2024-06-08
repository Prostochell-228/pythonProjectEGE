from ipaddress import *

for mask in range(0,33):
    net1 = ip_network(f'161.137.200.35/{mask}', False)
    net2 = ip_network(f'161.137.150.118/{mask}', False)
    if net1==net2:
        m = '1'*mask + '0'*(32-mask)
        print(m[16:24], int(m[16:24], 2))