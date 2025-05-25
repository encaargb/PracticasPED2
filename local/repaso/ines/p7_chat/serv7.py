#!/usr/bin/env python3
import socket
import select
import os
import setproctitle
import json
from collections import defaultdict

setproctitle.setproctitle("serv7")

IP = os.environ.get("CHAT_HOST", "0.0.0.0")
PUERTO = int(os.environ.get("CHAT_PORT", "12347"))
PASS_FILE = "passwords.json"

# Cargar contraseñas
if os.path.exists(PASS_FILE):
    with open(PASS_FILE, "r") as f:
        passwords = json.load(f)
else:
    passwords = {}

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((IP, PUERTO))
servidor.listen()

print(f"[serv7] Servidor escuchando en {IP}:{PUERTO}")

sockets_activos = [servidor]
nicks = {}
canales = defaultdict(set)  # canal → conjunto de sockets
usuarios = {}  # socket → canal
admin_nick = "admin"

try:
    while True:
        lectura, _, _ = select.select(sockets_activos, [], [])

        for sock in lectura:
            if sock == servidor:
                cliente, _ = servidor.accept()
                cliente.sendall(b"Nick: ")
                sockets_activos.append(cliente)
            else:
                try:
                    datos = sock.recv(1024).decode().strip()
                    if not datos:
                        raise ConnectionResetError

                    if sock not in nicks:
                        if ":" not in datos:
                            sock.sendall(b"[serv7] Formato de autenticacion invalido.\n")
                            sockets_activos.remove(sock)
                            sock.close()
                            continue

                        nick, hash_pass = datos.split(":", 1)

                        if nick in passwords and passwords[nick] != hash_pass:
                            sock.sendall(b"[serv7] Password incorrecto.\n")
                            sockets_activos.remove(sock)
                            sock.close()
                            continue
                        elif nick not in passwords:
                            passwords[nick] = hash_pass
                            with open(PASS_FILE, "w") as f:
                                json.dump(passwords, f)

                        if nick in nicks.values():
                            sock.sendall(b"[serv7] Nick duplicado.\n")
                            sockets_activos.remove(sock)
                            sock.close()
                        else:
                            nicks[sock] = nick
                            sock.sendall(b"Canal: ")
                    elif sock not in usuarios:
                        canal = datos
                        usuarios[sock] = canal
                        canales[canal].add(sock)
                        path = f"tmp/chat_{canal}.log"
                        if os.path.exists(path):
                            with open(path, 'r') as f:
                                ultimas = f.readlines()[-10:]
                                for l in ultimas:
                                    sock.sendall(l.encode())
                        aviso = f"[{nicks[sock]} se ha unido al canal {canal}]\n"
                        print(aviso.strip())
                        for otro in canales[canal]:
                            if otro != sock:
                                otro.sendall(aviso.encode())
                        sock.sendall(b"[serv7] Puedes escribir.\n")
                    else:
                        canal = usuarios[sock]
                        emisor = nicks[sock]

                        if datos.startswith("/msg "):
                            try:
                                _, destino, mensaje = datos.split(" ", 2)
                                for s, n in nicks.items():
                                    if n == destino:
                                        s.sendall(f"[privado] {emisor}: {mensaje}\n".encode())
                                        break
                            except:
                                sock.sendall(b"[serv7] Uso: /msg <nick> <mensaje>\n")

                        elif datos.startswith("/kick ") and emisor == admin_nick:
                            _, a_expulsar = datos.split(" ", 1)
                            for s, n in nicks.items():
                                if n == a_expulsar:
                                    s.sendall(b"[serv7] Has sido expulsado.\n")
                                    s.close()
                                    sockets_activos.remove(s)
                                    canales[canal].remove(s)
                                    del nicks[s]
                                    del usuarios[s]
                                    break

                        else:
                            texto = f"{emisor}: {datos}\n"
                            with open(f"tmp/chat_{canal}.log", "a") as f:
                                f.write(texto)
                            for otro in canales[canal]:
                                if otro != sock:
                                    otro.sendall(texto.encode())

                except:
                    if sock in nicks:
                        canal = usuarios.get(sock, None)
                        if canal:
                            canales[canal].discard(sock)
                        aviso = f"[{nicks[sock]} se ha desconectado.]\n"
                        print(aviso.strip())
                        for otro in canales[canal]:
                            otro.sendall(aviso.encode())
                        del usuarios[sock]
                        del nicks[sock]
                    if sock in sockets_activos:
                        sockets_activos.remove(sock)
                    sock.close()

except KeyboardInterrupt:
    print("\n[serv7] Servidor detenido. Notificando clientes...")
    for sock in sockets_activos:
        if sock != servidor:
            try:
                sock.sendall(b"[serv7] El servidor se ha apagado.\n")
                sock.close()
            except:
                pass
    servidor.close()
    print("[serv7] Apagado completo.")
