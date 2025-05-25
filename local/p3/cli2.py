# P2 - PIPES - CLIENTE

#!/usr/bin/env python3
import os

# Nombres de las pipes
pipe_in = "/tmp/pipe_cli2_serv2"
pipe_out = "/tmp/pipe_serv2_cli2"

# Escribir algo al servidor para activar la respuesta
with open(pipe_in, 'w') as pipe_write:
    pipe_write.write("get_time")

# Leer la respuesta del servidor
with open(pipe_out, 'r') as pipe_read:
    respuesta = pipe_read.read()

print("Fecha y hora del servidor:", respuesta)

