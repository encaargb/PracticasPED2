#!/usr/bin/env python3
import socket
import setproctitle

# Nombre del proceso
setproctitle.setproctitle("cli5")

# Dirección y puerto del servidor
SERVIDOR = "localhost"
PUERTO = 11111

# Crear socket UDP (IPv4)
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar mensaje vacío o "hora" (no importa el contenido)
cliente.sendto(b"hora", (SERVIDOR, PUERTO))

# Esperar respuesta
respuesta, _ = cliente.recvfrom(1024)

print("Fecha y hora del servidor:", respuesta.decode())

cliente.close()
