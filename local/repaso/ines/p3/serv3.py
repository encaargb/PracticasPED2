#!/usr/bin/env python3
import os

# Nombres personalizados de las FIFOs para el grupo 1
pipe_in = "/tmp/fifo_cli3_to_serv3_grupo1"
pipe_out = "/tmp/fifo_serv3_to_cli3_grupo1"

# Crear las FIFOs si no existen
if not os.path.exists(pipe_in):
    os.mkfifo(pipe_in)
if not os.path.exists(pipe_out):
    os.mkfifo(pipe_out)

# Leer la ruta del archivo enviada por el cliente
with open(pipe_in, 'r') as fifo_in:
    ruta = fifo_in.read().strip()

# Procesar la solicitud
try:
    with open(ruta, 'r') as f:
        contenido = f.read()
except Exception as e:
    contenido = f"[serv3] ERROR: No se pudo leer el archivo.\n{str(e)}"

# Enviar la respuesta al cliente
with open(pipe_out, 'w') as fifo_out:
    fifo_out.write(contenido)
