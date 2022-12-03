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
socketCon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Creación de la ventana
ancho = 500
alto = 500
ventana = pygame.display.set_mode( (ancho, alto) )
pygame.display.set_caption("|   T a l l e r    d e    S o c k e t s📨")
icono = pygame.image.load('icono.png')
ico = pygame.transform.scale(icono, (32,32) )
pygame.display.set_icon(icono)
idCliente = 0

class Jugador():
    def __init__(self, x, y, ancho, alto, color):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.rect = (x,y,ancho,alto)
        self.vel = 7
    
    def draw(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.ancho, self.alto)

def redibujarVentana(ventana, Jugador): 
    ventana.fill( (0,0,0) )
    Jugador.draw(ventana)
    pygame.display.update()


def main():
    socketCon.connect(DIRECCON)
    conexion = socketCon.recv(1024)
    run = True
    p = Jugador(50,50,100,100,(10,230,230))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                
                run = False
                pygame.quit()
                socketCon.send(exit)
        
        p.move()
        redibujarVentana(ventana, p)

main()

"""
while True:
    socketCon.connect(DIRECCON)
    conexion = socketCon.recv(1024)
    print(conexion.decode())
    exit = input("Te encuentras dentro del servidor, si deseas salir escribe: exit\n")
    socketCon.send(exit)
"""