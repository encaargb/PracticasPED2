#!/usr/bin/env python3
import socket
from datetime import datetime
import setproctitle

# Nombre del proceso
setproctitle.setproctitle("serv5")

# Puerto personalizado para tu grupo (por ejemplo 11111)
PUERTO = 11111

# Crear socket UDP (IPv4)
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("localhost", PUERTO))

print(f"[serv5] Esperando mensajes en el puerto {PUERTO}...")

try:
    while True:
        mensaje, direccion = servidor.recvfrom(1024)

        # Generar fecha y hora en formato ISO (sin microsegundos)
        fecha_hora = datetime.now().replace(microsecond=0).isoformat()

        servidor.sendto(fecha_hora.encode(), direccion)
        print(f"[serv5] Respondido a {direccion}")

except KeyboardInterrupt:
    print("\n[serv5] Servidor detenido por el usuario")
finally:
    servidor.close()
