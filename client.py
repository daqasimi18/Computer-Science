'''
Abdul Rehman Khurshid and Darab Ali Qasimi
client.py
'''
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from PIL import Image, ImageTk

# The IP address and the port number of the hosting server.
host_address = input('Enter the IP address of the host: ')
port_number = 8080

# Username that will be used in the chatroom as user's identity.
username = input("Choose a username: ")

def receive():
    '''
    This function receives messages from the server with a maximum size of 1024 bytes. 
    Each message is decoded by UTF-8 once received. 
 
    Parameters
    ----------
    None
 
    Returns
    -------
    None
    '''
    while True:
        try:
            message = client_socket.recv(1024).decode("utf8")
            message_list.insert(tkinter.END, message)
            if message == 'USER':
                client_socket.send(username.encode('ascii'))
        except:
            # If the user decides to do something that's prohibited, e.g. cleaning their username in the Chatroom
            # then they will be kicked out of the chatroom and they will get the following notification.
            print("You left the chatroom")
            break
            
def send():  
    '''
    This function sends the messages of the clients to the server.
 
    Parameters
    ----------
    None
 
    Returns
    -------
    None
    '''
    message = client_message.get()
    # The default entry of the message box is the user's username+":".
    client_message.set("{}: ".format(username))  
    client_socket.send(bytes(message, "utf8"))
    # Make a clone of user's username that looks the same as the default entry of the message box. 
    user_name = username + ":"
    split_message = message.split()
    # If the user enters /quit and nothing else then we interpret it as leaving the Chatroom
    # or if the user sent a message that doesn't contain user's username we will quit the Chatroom. 
    if split_message[-1] == "/quit" or split_message[0] != user_name:
        client_socket.close()
        chat_title.quit()

def close_chat():
    '''
    This function closes the chat if the user writes /quit.
 
    Parameters
    ----------
    None
 
    Returns
    -------
    None
    '''
    client_message.set("/quit")
    send()

# Chat title that appears at the top of the Chatroom    
chat_title = tkinter.Tk()
chat_title.title("EC Chatroom")

# Customized background of the Chatroom with an image.
background_image = Image.open("background_image.png")
background_image = background_image.resize((1500,800), Image.ANTIALIAS)
place_image = ImageTk.PhotoImage(background_image)

image_label = tkinter.Label(image=place_image)
image_label.image = place_image
image_label.place(x=0, y=0)

chat_frame = tkinter.Frame(chat_title)
client_message = tkinter.StringVar() 
# Enable the user to see their username in the message box starting from message 0.
client_message.set("{}: ".format(username))

# Chatroom is able to view your old and new messages through the use of scrollbars.
scrollbar = tkinter.Scrollbar(chat_frame)
horizontal_scrollbar = tkinter.Scrollbar(chat_frame, orient='horizontal')
message_list = tkinter.Listbox(chat_frame, height=15, width=80, yscrollcommand=scrollbar.set, xscrollcommand=horizontal_scrollbar.set, bg='gray82', fg='gray5', font=("Helvetica",12))
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
horizontal_scrollbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
scrollbar.config(command=message_list.yview)
horizontal_scrollbar.config(command=message_list.xview)
message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_list.place(x=100,y=200)
message_list.pack()
chat_frame.pack()

message_entry_box = tkinter.Entry(chat_title, textvariable=client_message)
message_entry_box.bind("<Return>", send)
message_entry_box.pack()

# Send button at the bottom of the message entry box.
send_button = tkinter.Button(chat_title, text="Send", command=send)
send_button.pack()
chat_title.protocol("WM_DELETE_WINDOW", close_chat)

# AF_INET is the address domain of the socket, and SOCK_STREAM is used for continuous flow of data.
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((host_address, port_number))

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()