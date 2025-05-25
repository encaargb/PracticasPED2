#!/usr/bin/env python3
import socket
import setproctitle

# Asignar nombre del proceso
setproctitle.setproctitle("cli6")

# Dirección y puerto del servidor (grupo 1)
IP = "localhost"
PUERTO = 11101

# Crear socket TCP (IPv4)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((IP, PUERTO))
    ruta = input("[cli6] Introduce la ruta del fichero: ")

    if not ruta:
        print("[cli6] Ruta vacía. Terminando cliente.")
        cliente.close()
        exit()

    cliente.sendall(ruta.encode())

    # Recibir respuesta del servidor
    datos = b""
    while True:
        parte = cliente.recv(1024)
        if not parte:
            break
        datos += parte

    print("\n[cli6] Respuesta del servidor:\n")
    print(datos.decode())

except Exception as e:
    print(f"[cli6] ERROR de conexión o recepción: {e}")

finally:
    cliente.close()
    print("[cli6] Cliente cerrado")
