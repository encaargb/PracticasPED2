#!/usr/bin/env python3
import os

# Nombres personalizados de las FIFOs
pipe_in = "/tmp/fifo_cli3_to_serv3_grupo1"
pipe_out = "/tmp/fifo_serv3_to_cli3_grupo1"

# Esperar a que el servidor haya creado las FIFOs
while not os.path.exists(pipe_in) or not os.path.exists(pipe_out):
    pass

# Leer la ruta del archivo a solicitar
ruta = input("[cli3] Introduce la ruta del archivo: ")

# Enviar la ruta al servidor
with open(pipe_in, 'w') as fifo_out:
    fifo_out.write(ruta)

# Leer la respuesta del servidor
with open(pipe_out, 'r') as fifo_in:
    respuesta = fifo_in.read()

print("\n[cli3] Respuesta del servidor:")
print(respuesta)
