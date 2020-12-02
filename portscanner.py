import socket
import tkinter as tk
from tkinter import *
import subprocess
import sys
from datetime import datetime
import time

subprocess.call('cls', shell=True)

host = input('Enter The IPV4 Of The Target: ') # ipv4 of the target where i want to perform a port scan

print("-"*60)
print('Please Wait, We Are Scanning The Targets Ports.....')
print("-"*60)

t1 = datetime.now()
time.sleep(3)

try:
	for portTCP in range(1,65535):
		sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sockTCP.settimeout(0.5)
		resultTCP = sockTCP.connect_ex((host, portTCP))
		if resultTCP == 0:
			print("PortTCP {}: \t Open".format(portTCP))
		sockTCP.close()

except KeyboardInterrupt:
	print('You Have killed The Scan Process By Pressing CTRL + C')
	sys.exit()

except socket.gaierror:
	print("The Given IPV4 Could Not Be found")
	sys.exit()

except socket.error:
	print("Could Not Connect To The Server")
	sys.exit()

t2 = datetime.now()
totalT = t1 -t2
totalT = str(totalT)
print("-"*60)
print('Scanning Completed In: ' + totalT)
print("-"*60)
