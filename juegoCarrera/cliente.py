import pygame
import numpy as np
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
ancho = 600
alto = 600
ventana = pygame.display.set_mode( (ancho, alto) )
pygame.display.set_caption("|   T a l l e r    d e    S o c k e t s ~ S i s t e m a s    D i s t r i b u i d o s📨")
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
        self.vel = 5
    
    def draw(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        
        if self.x < 0:
            self.x = 0
        
        if self.x > ancho-51:
            self.x = ancho-50

        if self.y < 0:
            self.y = 0      

        if self.y > ancho-51:
            self.y = ancho-50              
        
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
    randcolor = list(np.random.choice(range(256), size=3))
    player = Jugador(200,200,50,50, randcolor)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                
                run = False
                pygame.quit()
                socketCon.send(exit)
        
        player.move()
        redibujarVentana(ventana, player)

main()

"""
while True:
    socketCon.connect(DIRECCON)
    conexion = socketCon.recv(1024)
    print(conexion.decode())
    exit = input("Te encuentras dentro del servidor, si deseas salir escribe: exit\n")
    socketCon.send(exit)
"""