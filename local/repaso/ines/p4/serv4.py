#!/usr/bin/env python3
import socket
import os
import setproctitle

# Asignar nombre de proceso
setproctitle.setproctitle("serv4")

# Ruta del socket (configurable por variable de entorno)
SOCKET_PATH = os.environ.get("SOCKET_PATH", "/tmp/socket_grupo1")

# Eliminar socket anterior si existe
if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)

# Crear socket UDS
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
            with open(path, "rb") as f:
                contenido = f.read()

            # Intentar decodificar a texto
            try:
                contenido = contenido.decode()
            except:
                contenido = "[Fichero binario: no se puede mostrar como texto]"

        except Exception as e:
            contenido = f"[serv4] ERROR: {e}"

        # Enviar respuesta al cliente
        conexion.sendall(contenido.encode())
        conexion.close()

except KeyboardInterrupt:
    print("\n[serv4] Servidor detenido manualmente")

finally:
    servidor.close()
    if os.path.exists(SOCKET_PATH):
        os.remove(SOCKET_PATH)
    print("[serv4] Socket eliminado y servidor cerrado")
