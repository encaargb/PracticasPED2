#!/usr/bin/env python3
import socket
import select
import os
import setproctitle

setproctitle.setproctitle("serv7")

IP = os.environ.get("CHAT_HOST", "localhost")
PUERTO = int(os.environ.get("CHAT_PORT", "12347"))

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((IP, PUERTO))
servidor.listen()

print(f"[serv7] Servidor escuchando en {IP}:{PUERTO}")

sockets_activos = [servidor]
nicks = {}

try:
    while True:
        lectura, _, _ = select.select(sockets_activos, [], [])

        for sock in lectura:
            if sock == servidor:
                cliente, _ = servidor.accept()
                cliente.sendall("Introduce tu nick: ".encode())
                sockets_activos.append(cliente)
            else:
                try:
                    datos = b""
                    while True:
                        parte = sock.recv(1024)
                        if not parte:
                            raise ConnectionResetError
                        datos += parte
                        if len(parte) < 1024:
                            break

                    mensaje = datos.decode().strip()

                    if sock not in nicks:
                        if mensaje in nicks.values():
                            sock.sendall("[serv7] Nick duplicado. Conexión cerrada.\n".encode())
                            sockets_activos.remove(sock)
                            sock.close()
                        else:
                            nicks[sock] = mensaje
                            aviso = f"[{mensaje} se ha unido al chat.]\n"
                            print(aviso.strip())
                            for otro in nicks:
                                if otro != sock:
                                    otro.sendall(aviso.encode())
                            sock.sendall("[serv7] Conectado al chat.\n".encode())
                    else:
                        emisor = nicks[sock]
                        texto = f"{emisor}: {mensaje}\n"
                        print(texto.strip())
                        for otro in nicks:
                            if otro != sock:
                                otro.sendall(texto.encode())
                except:
                    if sock in nicks:
                        aviso = f"[{nicks[sock]} se ha desconectado.]\n"
                        print(aviso.strip())
                        del nicks[sock]
                        for otro in nicks:
                            otro.sendall(aviso.encode())
                    if sock in sockets_activos:
                        sockets_activos.remove(sock)
                    sock.close()
except KeyboardInterrupt:
    print("\n[serv7] Cerrando servidor...")
    for sock in sockets_activos:
        if sock != servidor:
            try:
                sock.sendall("[serv7] El servidor se ha detenido.\n".encode())
                sock.close()
            except:
                pass
    servidor.close()
    print("[serv7] Apagado completo.")
