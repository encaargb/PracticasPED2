# Práctica 7 - Sistema de Chat Cliente-Servidor (grupo1)

Este sistema implementa un servidor de chat multicanal con múltiples clientes simultáneos, autenticación segura por contraseña y varias funcionalidades avanzadas.

---

## 🚀 Ejecución rápida

### Servidor
```bash
make run_servidor
```

### Cliente (en otra terminal)
```bash
make run_cliente
```

---

## 👤 Manual de usuario

### Inicio del cliente
1. Introduce tu **nick** (único entre los conectados)
2. Introduce tu **contraseña** (se guarda cifrada SHA-256)
3. Introduce el **canal** (sala de chat, se crea si no existe)

### Comandos disponibles
- Enviar mensaje público: escribe y pulsa Enter
- Salir del chat:
  ```
  /salir
  ```
- Enviar mensaje privado:
  ```
  /msg <nick> <mensaje>
  ```
- Expulsar usuario (solo `admin`):
  ```
  /kick <nick>
  ```

### Histórico
- Al entrar en un canal se muestran los **últimos 10 mensajes** guardados en `tmp/chat_<canal>.log`

---

## ⚙️ Manual de instalación

### Requisitos
- Python 3.7 o superior
- Dependencias:
  ```bash
  pip install setproctitle
  ```

### Archivos necesarios
- `cli7.py` y `serv7.py`
- `Makefile`
- Carpeta `tmp/` (crear si no existe)
- Archivo `passwords.json` (se genera automáticamente)

---

## 🧱 Documento de arquitectura

### Componentes principales
- **Servidor (`serv7.py`)**:
  - Escucha conexiones TCP
  - Gestiona múltiples clientes simultáneamente con `select`
  - Verifica nicks únicos y contraseñas hash
  - Gestiona canales temáticos y el histórico
- **Cliente (`cli7.py`)**:
  - Se conecta a un servidor configurable (IP/puerto)
  - Envía nick, contraseña y canal
  - Escucha mensajes con `select` y permite comandos interactivos

### Archivos
- `passwords.json`: almacena hashes de contraseña (nunca en texto claro)
- `tmp/chat_<canal>.log`: guarda el histórico de cada canal

### Comunicación
- TCP, con protocolo simple de texto línea a línea
- Formato de autenticación: `nick:hash`

---

## ✅ Requisitos cumplidos

### Obligatorios
- ✅ Múltiples clientes simultáneos
- ✅ Nick único
- ✅ Parada limpia del servidor
- ✅ Configuración por variables
- ✅ Nombres de procesos `cli7`, `serv7`

### Opcionales
- ✅ Contraseña cifrada (SHA-256)
- ✅ Clientes y servidores de distintos grupos/sistemas
- ✅ Canales temáticos
- ✅ Histórico de conversaciones
- ✅ Mensajes privados
- ✅ Moderación (`/kick`)

---

¡Listo para entregar! 🎓
