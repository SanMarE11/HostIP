#!/usr/bin/python
import socket
def ipscan():
	host=raw_input("Ingresa el Host > ")
	hostf=host.replace("http://","")
	hostip=socket.gethostbyname(hostf)
	print("")
	print("		-------------------------------")
	print("			IP: "+hostip)
	print("		-------------------------------")
	ipscan()
try:
	ipscan()
except(KeyboardInterrupt, SystemExit):
	print("")
	print("\n \t [!]Session Terminada por el usuario")
	print("")

