#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket
import select


HEADER_LENGTH = 10

# Argumentos de entrada
IP = "127.0.0.1"
PORT = sys.argv[1]
PORT = int(PORT)

# Cria o objeto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# define ip e porta aplicado 
server_socket.bind((IP, PORT))

# faz server escutar novas conexoes
server_socket.listen()

# Lista as conexoes
sockets_list = [server_socket]
clients = {}
print(f'Listening for connections on {IP}:{PORT}...')

# Manipulaçao das mensagens recebidas 
def receive_message(client_socket):

    try:
        # obtem tamanho da msg
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        # retorna cabecalho da msg e os dados
        return {'header': message_header, 'data': client_socket.recv(message_length)}
    except:
        # Fecha o servidor
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    # Iterage com sockets
    for notified_socket in read_sockets:

        # se notrificar um novo socket
        if notified_socket == server_socket:
            # Aceita nova conexao
            client_socket, client_address = server_socket.accept()
            # Cliente manda seu username
            user = receive_message(client_socket)
            # se falso disconecta
            if user is False:
                continue
            # adiciona socket a lista
            sockets_list.append(client_socket)
            # salva username
            clients[client_socket] = user

            print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))

        # se socket existente manda msg
        else:
            # Recebe mensagem
            message = receive_message(notified_socket)
            # Se falso o cliente é desconectado 
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['data'].decode('utf-8')))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            # Pegar informaçao de quem enviou a msg
            user = clients[notified_socket]
            print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')
            # Interage com as mensgens dos clientes
            for client_socket in clients:
                if client_socket != notified_socket:
                    # Envia usuário e mensagem
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    # Manipula alguma excessoes se necessário
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]