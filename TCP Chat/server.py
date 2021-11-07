'''
Abdul Rehman Khurshid and Darab Ali Qasimi
server.py
'''
import socket
import threading

# The connection information of the server.
ip_address = '159.28.22.5'
port_number = 8080

# AF_INET is the address domain of the socket, and SOCK_STREAM is used for continuous flow of data.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_address, port_number))

# Listen to a maximum size of 1000 incoming connections.
# A maximum size of 1000 simultaneous connections represent the number of students and faculty at Earlham College. 
server.listen(1000)

users = []
usernames = []

def broadcast(message):
    '''
    This function sends messages to all the clients connected to the server.
 
    Parameters
    ----------
    message : str
             User's message
             
    Returns
    -------
    None
    '''
    for user in users:
        user.send(message)
        
def handle(user):
    '''
    This function hundles users and deals with special messages that act more like 
    a command. 
 
    Parameters
    ----------
    user : str
          EC Chatroom's user
          
    Returns
    -------
    None
    '''
    while True:
        try:
            message = user.recv(1024)
            broadcast(message)
        # If the server receives something other than a message this particular user will be treated as if they wrote "/quit".
        except:
            index = users.index(user)
            users.remove(user)
            user.close()
            username = usernames[index]
            broadcast('{} left!'.format(username).encode('ascii'))
            usernames.remove(username)
            break
                       
def receive():
    '''
    This function serves as a gateway for messages to get accepted to the server. 
    After clients get connected to the server each member of the Chatroom is also 
    being notified about the connection of a new user.
 
    Parameters
    ----------
    None
 
    Returns
    -------
    None
    '''
    while True:
        user, address = server.accept()
        print("Connected with {}".format(str(address)))
        user.send('USER'.encode('ascii'))
        # Receive message upto a size of 1024 bytes
        username = user.recv(1024).decode('ascii')
        # Avoid repeated usernames that might cause confusions
        if username not in usernames:
            usernames.append(username)
            users.append(user)
            # After a successful configuration let all the users know a new user joined the chatroom.
            print("{} Joined".format(username))
            broadcast("{} Joined! \n".format(username).encode('ascii'))
            user.send('Connected to the server!'.encode('ascii'))
            thread = threading.Thread(target=handle, args=(user,))
            thread.start()
        else:
            user.send("Duplicated username! Please try again with a different username.".encode('ascii'))
             
receive()