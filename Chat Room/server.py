import socket
import threading
import sys

server_add = 'localhost'
port_number = sys.argv[1]

clients = []
handles = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_add, int(port_number)))
server.listen()


def broadcast(message):
    for client in clients:
        client.send(message)

def handle_message(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            handle = handles[index]
            broadcast('{} left!'.format(handle).encode())
            handles.remove(handle)
            break

def receive_message():
    while True:
        client, address = server.accept()
        print("Connected to {}".format(str(address)))
        client.send('Handle'.encode())
        handle = client.recv(1024).decode()
        handles.append(handle)
        clients.append(client)
        client.send('Connected to server! \n'.encode())
        broadcast("{} Joined the chat room!".format(handle).encode())
        

        thread = threading.Thread(target=handle_message, args=(client,))
        thread.start()

receive_message()