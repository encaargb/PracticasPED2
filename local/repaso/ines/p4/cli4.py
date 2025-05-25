#!/usr/bin/env python3
import socket
import os
import setproctitle

# Asignar nombre de proceso
setproctitle.setproctitle("cli4")

# Ruta del socket (configurable por variable de entorno)
SOCKET_PATH = os.environ.get("SOCKET_PATH", "/tmp/socket_grupo1")

# Solicitar al usuario la ruta del archivo
ruta = input("[cli4] Introduce la ruta del fichero: ")
if not ruta:
    print("[cli4] Ruta vacía. Terminando cliente.")
    exit()

# Crear socket UDS
cliente = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

try:
    cliente.connect(SOCKET_PATH)
    cliente.sendall(ruta.encode())

    # Recibir respuesta del servidor
    datos = b""
    while True:
        parte = cliente.recv(1024)
        if not parte:
            break
        datos += parte

    print("\n[cli4] Respuesta del servidor:\n")
    print(datos.decode())

except Exception as e:
    print(f"[cli4] ERROR al conectarse o recibir datos: {e}")

finally:
    cliente.close()
    print("[cli4] Cliente finalizado.")
