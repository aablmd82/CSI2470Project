# client.py ver 1.0.0
# 12/1/2017 Sean Dallas

from socket import *
from struct import pack


class ClientProtocol:

    def __init__(self):
        self.socket = None

    def connect(self, server_ip, server_port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((server_ip, server_port))

    def close(self):
        self.socket.shutdown(SHUT_WR)
        self.socket.close()
        self.socket = None

    def send_image(self, image_data):

        # use struct to make sure we have a consistent endianness on the length
        length = pack('>Q', len(image_data))

        # sendall to make sure it blocks if there's back-pressure on the socket
        self.socket.sendall(length)
        self.socket.sendall(image_data)


if __name__ == '__main__':
    cp = ClientProtocol()

    image_data = None
    with open('IMG_0077.jpg', 'r') as fp:
        image_data = fp.read()

    assert(len(image_data))
    cp.connect('127.0.0.1', 55555)
    cp.send_image(image_data)
    cp.close()








##import socket                   # Import socket module
##
##s = socket.socket()             # Create a socket object
##host = socket.gethostname()     # Get local machine name
##port = 60000                    # Reserve a port for your service.
##
##s.connect((host, port))
##s.send(("Hello server!").encode())
##
##def transfer(image):
##        s.send((image).encode())
####with open('received_file', 'wb') as f:
####    print ("file opened")
####    while True:
####        print("receiving data...")
####        data = s.recv(1024)
####        print("data =%s", (data))
####        if not data:
####            break
####        # write data to a file
####        f.write(data)
####
####f.close()
####print('Successfully get the file')
##while True:
##        print("receiving data...")
##        data = s.recv(1024)
##        print("data =%s", (data).decode())
##        if not data:
##            break
##s.close()
##print('connection closed')
