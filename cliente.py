import socket
import sys
 
# Crear socket
socketConexion = socket.socket()
 
puerto = int(input("Introduzca el puerto de conexión: "))
 
try:
    socketConexion.connect(('localhost', puerto))
except socket.error as message:
    print("Falló la conexión a través del puerto {}".format(puerto))
    print(message)
    sys.exit()  
 
# Recibir y mostrar el mensaje del servidor
mensajeServidor = socketConexion.recv(1024)
print(mensajeServidor.decode())

socketConexion.close()