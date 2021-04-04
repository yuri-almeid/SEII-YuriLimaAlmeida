#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket


door = sys.argv[1]
filename = sys.argv[2]

print(door)

door = int(door)

with open(filename,'r') as file:
    data = file.read()
print(data)



# Cria o objeto Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), door))
s.listen(5)



# Envia a msg
while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes(data,"utf-8"))
    clientsocket.close()