import socket
import threading
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((sys.argv[1], int(sys.argv[2])))
handle = sys.argv[3]

def receive_message():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'Handle':
                client.send(handle.encode())
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break
def compose():
    while True:
    	user_input = input('')
    	processed = "."
    	if user_input[0] == '.':
    		processed += user_input
    	else:
    		processed = user_input
    	message = '{}: {}'.format(handle, processed)
    	client.send(message.encode())

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

write_thread = threading.Thread(target=compose)
write_thread.start()

