import multiprocessing
import os
import sys

def servidor(conn):
    print("[serv2] Servidor iniciado. Esperando ruta de archivo...")
    filepath = conn.recv()
    print(f"[serv2] Ruta recibida: {filepath}")

    try:
        with open(filepath, 'r') as f:
            contenido = f.read()
        respuesta = f"[serv2] Archivo leído correctamente:\n\n{contenido}"
    except Exception as e:
        respuesta = f"[serv2] ERROR: No se pudo leer el archivo.\n{str(e)}"

    conn.send(respuesta)
    conn.close()
    print("[serv2] Respuesta enviada. Terminando proceso servidor.")


def cliente(conn, filepath):
    print("[cli2] Cliente iniciado.")
    conn.send(filepath)
    print("[cli2] Ruta enviada al servidor. Esperando respuesta...")

    respuesta = conn.recv()
    print("\n[cli2] Respuesta del servidor:\n")
    print(respuesta)
    conn.close()
    print("[cli2] Cliente finalizado.")


def main():
    print("[cliserv2] Iniciando sistema cliente-servidor con pipes en Windows")
    filepath = input("[cli2] Introduce la ruta completa del archivo a leer: ")

    parent_conn, child_conn = multiprocessing.Pipe()

    p_serv = multiprocessing.Process(target=servidor, args=(child_conn,), name="serv2")
    p_cli = multiprocessing.Process(target=cliente, args=(parent_conn, filepath), name="cli2")

    p_serv.start()
    p_cli.start()

    p_cli.join()
    p_serv.join()
    print("[cliserv2] Interacción finalizada. Ambos procesos han terminado.")

if __name__ == '__main__':
    multiprocessing.freeze_support()  # Para compatibilidad con Windows
    main()