#!/usr/bin/python
import socket
def ipscan():
	print("")
	print("   #####################################################")
	print("   #						       #")
	print("   #    _  _   _  __                 _    ___  _____   #")
	print("   #  _| || |_| |/ /                | |  / _ \| ____|  #")
	print("   # |_  __  _| ' / _ __ _   _ _ __ | |_| | | | |__    #")
	print("   #  _| || |_|  < | '__| | | | '_ \| __| | | |___ \   #")
	print("   # |_  __  _| . \| |  | |_| | |_) | |_| |_| |___) |  #")
	print("   #   |_||_| |_|\_\_|   \__, | .__/ \__|\___/|____/   #")
	print("   #      ______          __/ | |                      #")
	print("   #     |______|        |___/|_|                      #")
	print("   #						       #")
	print("   # FanPage: https://www.facebook.com/Krypt05Oficial/ #")
	print("   # Youtube: https://goo.gl/npgx85		       #")
	print("   #						       #")
	print("   #####################################################")
	print("")
	print("")
	
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

