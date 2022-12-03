import pygame
import threading
import socket
import time
import sys

#Creación de ventana
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('test')

#Creación y conexion de socket
SERVER = 'localhost'
PUERTO = 8000
DIRECCON = (SERVER,PUERTO)
socketAct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketAct.bind(DIRECCON)

def manejarCliente(conn, addr):#Función encargada de gestionar la comunicacion entre el cliente y el servidor
    print(f"Conexion exitosa de {addr}.")
    saludo = f"Bienvenido usuario {addr[1]}"
    conn.send(saludo.encode())
    salir = conn.recv(1024)
    if salir == "exit":
        conn.close()
    print (f"El usuario {addr[1]} se ha desconectado")
    conn.send(salir)
    

def iniciar():#Función encargada de gestionar las nuevas conexiones
    socketAct.listen(5)
    while True:
        conn, addr = socketAct.accept()
        thread = threading.Thread(target=manejarCliente, args=(conn, addr))
        thread.start()
        print(f"[Conexiones activas] {threading.active_count() - 1}")

iniciar()
