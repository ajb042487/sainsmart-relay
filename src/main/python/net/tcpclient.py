import socket
import sys

class TcpClient():
    def __init__(self):
        self.sock = None

    def connect(self, address, port):
        server_address = (address, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(server_address)

    def disconnect(self):
        self.sock.close()

    def read(self, data, length):
        data = bytearray(self.sock.recv(length))

    def write(self, data):
        self.sock.sendall(bytearray(data))
