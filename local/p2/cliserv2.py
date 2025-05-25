#!/usr/bin/env python3
import os
from datetime import datetime
import setproctitle

# Crear dos tuberías anónimas (una para cada dirección)
r1, w1 = os.pipe()  # cliente escribe, servidor lee
r2, w2 = os.pipe()  # servidor escribe, cliente lee

pid = os.fork()

if pid == 0:
     # Proceso hijo: servidor (serv2)
    setproctitle.setproctitle("serv2")
    
    os.close(w1)  # no escribe en pipe1
    os.close(r2)  # no lee de pipe2

    # Leer petición del cliente
    with os.fdopen(r1, 'r') as pipe_lectura:
        mensaje = pipe_lectura.read()

    # Generar fecha y hora en formato ISO (sin microsegundos)
    fecha_hora = datetime.now().replace(microsecond=0).isoformat()

    # Enviar la respuesta al cliente
    with os.fdopen(w2, 'w') as pipe_escritura:
        pipe_escritura.write(fecha_hora)

else:
    # Proceso padre: cliente (cli2)
    setproctitle.setproctitle("cli2")
    
    os.close(r1)  # no lee de pipe1
    os.close(w2)  # no escribe en pipe2

    # Enviar petición al servidor
    with os.fdopen(w1, 'w') as pipe_escritura:
        pipe_escritura.write("get_time")

    # Leer respuesta del servidor
    with os.fdopen(r2, 'r') as pipe_lectura:
        respuesta = pipe_lectura.read()

    print("Fecha y hora del servidor:", respuesta)

