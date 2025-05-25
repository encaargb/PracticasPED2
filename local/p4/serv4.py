#!/usr/bin/env python3
import socket
import os
import setproctitle

setproctitle.setproctitle("serv4")

SOCKET_PATH = os.environ.get("SOCKET_PATH", "/tmp/socket_grupo12")

if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)

servidor = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
servidor.bind(SOCKET_PATH)
servidor.listen()

print(f"[serv4] Servidor escuchando en {SOCKET_PATH}")

try:
    while True:
        conexion, _ = servidor.accept()
        print("[serv4] Cliente conectado")

        # Recibir la ruta del fichero
        path = conexion.recv(1024).decode()

        try:
            f = open(path, "rb")  # Abrimos en binario
            contenido = f.read()
            f.close()

             # Intentamos convertir a texto
            try:
                contenido = contenido.decode()
            except:
                contenido = "[Fichero binario: no se puede mostrar como texto]"
                
        except Exception as e:
            contenido = f"ERROR: {e}"

        # Enviar el contenido o error
        conexion.sendall(contenido.encode())
        conexion.close()

except KeyboardInterrupt:
    print("\n[serv4] Servidor detenido por el usuario")

finally:
    servidor.close()
    if os.path.exists(SOCKET_PATH):
        os.remove(SOCKET_PATH)
    print("[serv4] Socket eliminado")
