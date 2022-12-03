import pygame
import threading
import socket
import time
import os
import sys

#Creación y conexion de socket
SERVER = 'localhost'
PUERTO = 8000
DIRECCON = (SERVER,PUERTO)
socketCon = socket.socket()

while True:
    socketCon.connect(DIRECCON)
    conexion = socketCon.recv(1024)
    print(conexion.decode())
    exit = input("Te encuentras dentro del servidor, si deseas salir escribe: exit\n")
    socketCon.send(exit)
    if mensaje == "salir":
        socketCon.close()