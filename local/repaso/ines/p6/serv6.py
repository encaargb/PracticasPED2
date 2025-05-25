#!/usr/bin/env python3
import socket
import os
import setproctitle

# Asignar nombre del proceso
setproctitle.setproctitle("serv6")

# Dirección y puerto personalizados para grupo 1
IP = "localhost"
PUERTO = 11101

# Crear socket TCP (IPv4)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IP, PUERTO))
servidor.listen()

print(f"[serv6] Servidor TCP escuchando en {IP}:{PUERTO}")

try:
    while True:
        conexion, direccion = servidor.accept()
        print(f"[serv6] Cliente conectado desde {direccion}")

        try:
            path = conexion.recv(1024).decode()

            try:
                with open(path, "rb") as f:
                    contenido = f.read()

                try:
                    contenido = contenido.decode()
                except:
                    contenido = "[Fichero binario: no se puede mostrar como texto]"

            except Exception as e:
                contenido = f"[serv6] ERROR: No se pudo leer el archivo.\n{e}"

            conexion.sendall(contenido.encode())

        except Exception as e:
            print(f"[serv6] Error al manejar la petición: {e}")
        finally:
            conexion.close()

except KeyboardInterrupt:
    print("\n[serv6] Servidor detenido manualmente")

finally:
    servidor.close()
    print("[serv6] Socket cerrado")
