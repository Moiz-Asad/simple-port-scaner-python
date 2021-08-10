#!/bin/python

import sys
import socket
from datetime import datetime as dt
import re

print("Running State.....")
# Validating Ip Address
def isValidIP(IP):
    Ls = IP.split(".")
    regex = '^[0-9]+$'
    if (len(Ls) <4):
        return False
    for i in Ls:
        if re.search(regex,i):
            if int(i) > 255 and int(i) < 0:
                return False
    return True

# Input arguments
if len(sys.argv) == 2 and isValidIP(sys.argv[1]):
    Target = socket.gethostbyname(sys.argv[1])
else:
    print("Syntax Error!")
    print("Invalid Arguments.")
    print("Syntax : python <FileName>.py <IP-Address>")
    sys.exit()

init = 1
terminal = 90

print("----------------------------------")
print("            PORT Scanner          ")
print("----------------------------------")
print("Starting Scanning......")


# Trying available ports
try:
    Lst = []
    p = 0
    p1 = 0
    p2 = 0
    for port in range(init,terminal):
        print("PORT Scanning : {}".format(port))
        p+=1
        newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        Res = newSocket.connect_ex((Target,port))
        if Res == 0:
            Lst.append(port)
            p1 +=1
        else:
            p2+=1
        newSocket.close()
    print("----------------------------------")
    for i in Lst:
        print("PORT {} is open.".format(i))
    print("----------------------------------")
    print("       Total PORTs scanned {}".format(p))
    print("       Open PORTs {}".format(p1))
    print("       Close PORTs {}".format(p2))
    print("----------------------------------")
# Keyboard interupt occures
except KeyboardInterrupt:
    print("\nProgram Exited. (Reason: Keyboard Interupt)")
    sys.exit()

# Can't Find Host Name
except socket.gaierror:
    print("Hostname can't be resolved.")
    sys.exit()

# If Server isn't Running
except socket.error:
    print("Can't Connect to the Server at this Time. Try again later!")
    sys.exit()
