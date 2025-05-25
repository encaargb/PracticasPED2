import multiprocessing
from datetime import datetime

def servidor(conn):
    print("[serv2] Servidor iniciado. Esperando solicitud...")
    mensaje = conn.recv()
    print(f"[serv2] Mensaje recibido: {mensaje}")

    if mensaje == "get_time":
        fecha_hora = datetime.now().replace(microsecond=0).isoformat()
        respuesta = f"[serv2] Fecha y hora: {fecha_hora}"
    else:
        respuesta = "[serv2] ERROR: Mensaje no reconocido."

    conn.send(respuesta)
    conn.close()
    print("[serv2] Respuesta enviada. Terminando proceso servidor.")

def cliente(conn):
    print("[cli2] Cliente iniciado. Enviando solicitud de fecha y hora...")
    conn.send("get_time")
    respuesta = conn.recv()
    print("\n[cli2] Respuesta del servidor:")
    print(respuesta)
    conn.close()
    print("[cli2] Cliente finalizado.")

def main():
    print("[cliserv2] Iniciando sistema cliente-servidor de fecha/hora")
    parent_conn, child_conn = multiprocessing.Pipe()

    p_serv = multiprocessing.Process(target=servidor, args=(child_conn,), name="serv2")
    p_cli = multiprocessing.Process(target=cliente, args=(parent_conn,), name="cli2")

    p_serv.start()
    p_cli.start()

    p_cli.join()
    p_serv.join()
    print("[cliserv2] Interacción finalizada. Ambos procesos han terminado.")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
