#!/usr/bin/env python3
import socket
import select
import sys
import os
import setproctitle
import hashlib

setproctitle.setproctitle("cli7")

IP = os.environ.get("CHAT_HOST", "localhost")
PUERTO = int(os.environ.get("CHAT_PORT", "12347"))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((IP, PUERTO))
except:
    print("[cli7] No se pudo conectar al servidor.")
    exit()

# Recibir solicitud de nick
print(sock.recv(1024).decode(), end="")
nick = input().strip()
if not nick:
    print("[cli7] Nick vacío. Saliendo.")
    sock.close()
    exit()

# Pedir contraseña
password = input("Password: ").strip()
if not password:
    print("[cli7] Contraseña vacía. Saliendo.")
    sock.close()
    exit()

# Calcular hash y enviar nick:hash
hash_pass = hashlib.sha256(password.encode()).hexdigest()
sock.sendall(f"{nick}:{hash_pass}".encode())

# Recibir solicitud de canal
print(sock.recv(1024).decode(), end="")
canal = input().strip()
if not canal:
    print("[cli7] Canal vacío. Saliendo.")
    sock.close()
    exit()

sock.sendall(canal.encode())

# Mostrar mensajes iniciales del servidor
while True:
    parte = sock.recv(1024)
    print(parte.decode(), end="")
    if len(parte) < 1024:
        break

print("[cli7] Puedes escribir. Usa /salir para salir, /msg y /kick según el canal.\n")

try:
    while True:
        lectura, _, _ = select.select([sys.stdin, sock], [], [])

        for fuente in lectura:
            if fuente == sock:
                datos = sock.recv(1024)
                if not datos:
                    print("\n[cli7] El servidor cerró la conexión.")
                    sock.close()
                    exit()
                print(datos.decode(), end="")
            else:
                mensaje = sys.stdin.readline().strip()
                if mensaje == "/salir":
                    print("[cli7] Saliendo del chat.")
                    sock.close()
                    exit()
                sock.sendall(mensaje.encode())

except KeyboardInterrupt:
    print("\n[cli7] Cliente interrumpido.")
    sock.close()
