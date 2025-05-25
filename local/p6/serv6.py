#!/usr/bin/env python3
import socket
import os
import setproctitle

setproctitle.setproctitle("serv6")

IP = "localhost"
PUERTO = 11111

# Crear socket TCP (IPv4)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IP, PUERTO))
servidor.listen()

print(f"[serv6] Servidor escuchando en {IP}:{PUERTO}")

try:
    while True:
        conexion, direccion = servidor.accept()
        print(f"[serv6] Conectado a {direccion}")

        try:
            path = conexion.recv(1024).decode()

            try:
                f = open(path, "rb")  # Leer como binario
                contenido = f.read()
                f.close()

                try:
                    contenido = contenido.decode()
                except:
                    contenido = "[Fichero binario: no se puede mostrar como texto]"

            except Exception as e:
                contenido = f"ERROR: {e}"

            conexion.sendall(contenido.encode())

        except Exception as e:
            print(f"[serv6] Error al manejar la petición: {e}")
        finally:
            conexion.close()

except KeyboardInterrupt:
    print("\n[serv6] Servidor detenido por el usuario")
finally:
    servidor.close()
    print("[serv6] Socket cerrado")
