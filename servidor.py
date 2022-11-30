
import socket
import sys
 
# Crear socket
socketAbierto = socket.socket()

puerto = int(input("Introduzca el puerto de escucha: "))
 
try:
    socketAbierto.bind(('localhost', puerto))
except socket.error as message:
    print("Falló la escucha por el puerto {}".format(puerto), ". Intente con otro puerto.")
    print(message)
    sys.exit()

# Iniciamos la escucha
socketAbierto.listen()
print("Escuchando en el puerto: ", puerto)
while True:
    # A la espera de una conexión de un cliente
    connection,address = socketAbierto.accept()
    print("Cliente Nº", address[1], "conectado a través de la ip", address[0])
   
    # Enviar un mensaje al cliente conectado
    mensaje = "Mensaje enviado al cliente desde el servidor"
    connection.send(mensaje.encode())
    
    connection.close()
