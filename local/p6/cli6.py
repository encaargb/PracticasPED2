#!/usr/bin/env python3
import socket
import setproctitle

setproctitle.setproctitle("cli6")

IP = "localhost"
PUERTO = 11111

# Crear socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((IP, PUERTO))

    ruta = input("Introduce la ruta del fichero: ")
    if not ruta:
        print("[cli6] Ruta vacía, no se envía nada al servidor.")
        cliente.close()
        exit()
    cliente.sendall(ruta.encode())

    # Bucle para recibir todo el contenido del servidor
    datos = b""
    while True:
        parte = cliente.recv(1024)
        if not parte:
            break
        datos += parte    
    
    print("Contenido recibido:\n", datos.decode())
    
except Exception as e:
    print(f"[cli6] Error de conexión o recepción: {e}")

finally:
    cliente.close()
