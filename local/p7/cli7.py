#!/usr/bin/env python3
import socket
import select
import sys
import os
import setproctitle

setproctitle.setproctitle("cli7")

IP = os.environ.get("CHAT_HOST", "localhost")
PUERTO = int(os.environ.get("CHAT_PORT", "12347"))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((IP, PUERTO))
except:
    print("[cli7] No se pudo conectar al servidor.")
    exit()

# Recibir mensaje de bienvenida (usando bucle)
datos = b""
while True:
    parte = sock.recv(1024)
    datos += parte
    if len(parte) < 1024:
        break

print(datos.decode(), end="")

nick = input().strip()
if not nick:
    print("[cli7] Nick vacío. Terminando cliente.")
    sock.close()
    exit()

sock.sendall(nick.encode())

# Esperar confirmación
datos = b""
while True:
    parte = sock.recv(1024)
    datos += parte
    if len(parte) < 1024:
        break

respuesta = datos.decode()
print(respuesta, end="")
if "rechazada" in respuesta:
    sock.close()
    exit()

print("[cli7] Puedes escribir mensajes. Usa /salir para salir.\n")

try:
    while True:
        lectura, _, _ = select.select([sys.stdin, sock], [], [])

        for fuente in lectura:
            if fuente == sock:
                datos = b""
                while True:
                    parte = sock.recv(1024)
                    if not parte:
                        print("\n[cli7] El servidor cerró la conexión.")
                        sock.close()
                        exit()
                    datos += parte
                    if len(parte) < 1024:
                        break
                print(datos.decode().strip())
            else:
                mensaje = sys.stdin.readline().strip()
                if mensaje == "/salir":
                    print("[cli7] Saliendo del chat.")
                    sock.close()
                    exit()
                sock.sendall(mensaje.encode())

except KeyboardInterrupt:
    print("\n[cli7] Interrumpido por el usuario.")
    sock.close()
