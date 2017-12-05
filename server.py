# server.py ver 1.0.0
# 12/1/2017 Sean Dallas
from socket import *
from struct import unpack


class Server:

    def __init__(self):
        self.socket = None

    def listen(self, server_ip, server_port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((server_ip, server_port))
        self.socket.listen(1)

    def retrieve_data(self, listener):

        try:
            while True:
                (connection, addr) = self.socket.accept()
                try:
                    bs = connection.recv(8)
                    (length,) = unpack('>Q', bs)
                    data = b''
                    while len(data) < length:
                        # doing it in batches is generally better than trying
                        # to do it all in one go, so I believe.
                        to_read = length - len(data)
                        data += connection.recv(
                            4096 if to_read > 4096 else to_read)

                finally:
                    connection.shutdown(SHUT_WR)
                    connection.close()

                listener(data)

        finally:
            self.close()

    def close(self):
        self.socket.close()
        self.socket = None


##
##
##port = 60000                    # Reserve a port for your service.
##s = socket.socket()             # Create a socket object
##host = socket.gethostname()     # Get local machine name
##s.bind((host, port))            # Bind to the port
##s.listen(5)                     # Now wait for client connection.
##
##print ("Server listening....")
##
##while True:
##    conn, addr = s.accept()     # Establish connection with client.
##    print ("Got connection from", str(addr))
##
##
##    data = conn.recv(1024)
##    print('Server received', (data).decode())
##    print('Done sending')
##    conn.send(('Thank you for connecting').encode())
##    conn.close()
