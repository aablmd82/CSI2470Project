import sys
from datetime import datetime
from scapy.all import srp,Ether,ARP,conf
import socket

def run(port):
    found = False
    server_address = '0.0.0.0'

    while found == False:
        ips = socket.gethostbyname(socket.gethostname()).rstrip('0123456789') + "0/24"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2,inter=0.1)
        for snd,rcv in ans:
            attempt_address = (str(rcv.psrc), port)
            if (s.connect_ex(attempt_address) == 0):
                found = True
                server_address = str(rcv.psrc)
    return server_address
