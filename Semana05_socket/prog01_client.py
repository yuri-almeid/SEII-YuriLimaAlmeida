#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket

door = sys.argv[1]
ip = sys.argv[2]
filename = sys.argv[3]


door = int(door)
# nao estou usando o IP porque estou fazendo na mesma maquina e rede local


# Cria objeto
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), door))

print('Salvando dados...')
# Recebe e printa msg
msg = s.recv(door)
out = msg.decode("utf-8")


file = open(filename,'w') 
file.write(out) 
file.close() 
