# P2 - PIPES - SERVIDOR


#!/usr/bin/env python3
import os
import time
from datetime import datetime

# Nombres de las pipes
pipe_in = "/tmp/pipe_cli2_serv2"
pipe_out = "/tmp/pipe_serv2_cli2"

# Crear las pipes si no existen
if not os.path.exists(pipe_in):
    os.mkfifo(pipe_in)
if not os.path.exists(pipe_out):
    os.mkfifo(pipe_out)

# Leer cualquier cosa del cliente (solo para activar la respuesta)
with open(pipe_in, 'r') as pipe_read:
    pipe_read.read()  # No usamos el contenido, solo activamos la respuesta

# Obtener fecha y hora en formato estándar ISO
fecha_hora = datetime.now().replace(microsecond=0).isoformat()

# Enviar la fecha y hora al cliente
with open(pipe_out, 'w') as pipe_write:
    pipe_write.write(fecha_hora)

