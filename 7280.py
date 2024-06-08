from ipaddress import *

for mask in range(0, 33):
    net1 = ip_network(f'176.213.225.119/{mask}', False)
    net2 = ip_network(f'176.213.195.58/{mask}', False)
    if net1 == net2:
        m = '1' * mask + '0' * (32 - mask)
        print(m[16:24], int(m[16:24], 2))
