# server.py ver 1.0.0
# 12/1/2017 Sean Dallas
from os import *
from socket import *                   # Import socket module ABLEMIND
from struct import unpack


class Server:

    def __init__(self):
        self.socket = None
        self.output_dir = '.'
        self.file_num = 1

    def listen(self, server_ip, server_port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((server_ip, server_port))
        self.socket.listen(1)

    def handle_images(self):

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

                    # send our 0 ack
                    #assert len(b'\00') == 1
                    #connection.sendall(b'\00')  i don't think this assert is needed
                finally:
                    connection.shutdown(SHUT_WR)
                    connection.close()

                with open(os.path.join(
                        self.output_dir, '%06d.jpg' % self.file_num), 'w'
                ) as fp:
                    fp.write(data)

                self.file_num += 1
        finally:
            self.close()

    def close(self):
        self.socket.close()
        self.socket = None


     # could handle a bad ack here, but we'll assume it's fine.

if __name__ == '__main__':
    sp = Server()
    sp.listen('127.0.0.1', 55555)
    sp.handle_images()





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
