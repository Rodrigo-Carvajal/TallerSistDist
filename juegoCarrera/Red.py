import socket

class Red:
    def __init__(self):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER = 'localhost'
        self.PUERTO = 8000
        self.DIRECCION = (self.SERVER, self.PUERTO)
        self.id = self.connect()
        
    def connect(self):
        try:
            self.cliente.connect(self.addr)
            return self.cliente.recv(2048).decode()
        except:
            pass

n = Red()
