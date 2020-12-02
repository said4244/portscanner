import socket
import tkinter as tk
from tkinter import *
import subprocess
import sys
from datetime import datetime
import time

subprocess.call('cls', shell=True)

host = input('Vul in de IPv4 van het doelwit: ') # ipv4 van de doelwit, die er gescant gaat worden

print("-"*60)
print('Even wachten, we zijn de poorten aan het scannen.....')
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
	print("de gegeven IPv4 kan niet gevonden worden")
	sys.exit()

except socket.error:
	print("Kan niet connecten met de server :(")
	sys.exit()

t2 = datetime.now()
totalT = t1 -t2
totalT = str(totalT)
print("-"*60)
print('Scanning Completed In: ' + totalT)
print("-"*60)
