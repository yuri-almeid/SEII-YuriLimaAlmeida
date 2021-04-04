#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket
import select
import errno

HEADER_LENGTH = 10


# Argumentos de entrada
IP = sys.argv[1]
PORT = sys.argv[2]
my_username = sys.argv[3]

PORT = int(PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta com IP e PORTA específico
client_socket.connect((IP, PORT))

# Define conexao para nao bloqueável
client_socket.setblocking(False)

# Prepara e envia o username do usuário
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:

    # Aguarda msg do usuário
    message = input(f'{my_username} > ')

    # se msg é não vazia manda
    if message:

        # Faz o encode da msg e envia
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        # Loop para receber msg
        while True:

            # obtem tamanho da msg
            username_header = client_socket.recv(HEADER_LENGTH)

            # Se não receber dados
            if not len(username_header):
                print('Connection closed by the server')
                sys.exit()

            username_length = int(username_header.decode('utf-8').strip())

            # Recebe e decodifica Username
            username = client_socket.recv(username_length).decode('utf-8')

            # faz o mesmo para a msg
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            # Mostra mensagem
            print(f'{username} > {message}')

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # Se nao receber msg, toca o pau
        continue

    except Exception as e:
        # Se ocorrer algum problema fecha
        print('Reading error: '.format(str(e)))
        sys.exit()