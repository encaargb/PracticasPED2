#!/usr/bin/env python3
import socket
import setproctitle

# Asignar nombre del proceso
setproctitle.setproctitle("cli5")

# Dirección y puerto del servidor (grupo 1)
SERVIDOR = "localhost"
PUERTO = 11101

# Crear socket UDP (IPv4)
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Enviar mensaje (puede ser "hora" o vacío)
    cliente.sendto(b"hora", (SERVIDOR, PUERTO))

    # Esperar respuesta del servidor
    respuesta, _ = cliente.recvfrom(1024)
    print("[cli5] Fecha y hora del servidor:", respuesta.decode())

except Exception as e:
    print(f"[cli5] ERROR al comunicarse con el servidor: {e}")

finally:
    cliente.close()
    print("[cli5] Cliente cerrado")
