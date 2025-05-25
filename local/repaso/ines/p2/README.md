# Práctica 2 - Cliente-Servidor con Pipes en Python (Windows)

Este proyecto incluye dos aplicaciones cliente-servidor independientes utilizando pipes anónimos (adaptados para Windows mediante `multiprocessing.Pipe()`). Ambas están implementadas en un único script que lanza dos procesos (`cli2` y `serv2`) y cumplen los requisitos del enunciado original.

---

## Aplicación 1: Cliente-servidor de ficheros

### Archivo principal
`cliserv2.py` o `cliserv2_win.py` (dependiendo de cómo lo hayas organizado)

### Funcionamiento
- El cliente (`cli2`) pide al usuario una **ruta de archivo**.
- Envía la ruta al servidor (`serv2`) mediante un pipe.
- El servidor intenta leer el archivo y devuelve:
  - Su contenido, si puede leerlo.
  - Un mensaje de error, si no.
- El cliente muestra la respuesta en pantalla.

### Ejecución
```bash
python cliserv2_win.py
```

---

## Aplicación 2: Cliente-servidor de fecha y hora

### Archivo principal
`cliserv2_fecha.py`

### Funcionamiento
- El cliente (`cli2`) envía la cadena `"get_time"` al servidor.
- El servidor (`serv2`) responde con la **fecha y hora actual** en formato ISO (sin microsegundos).
- El cliente muestra la respuesta.

### Ejecución
```bash
python cliserv2_fecha.py
```

---

## Notas importantes

- Se ha utilizado `multiprocessing.Pipe()` y `multiprocessing.Process` ya que `os.fork()` y `os.pipe()` **no están disponibles en Windows**.
- Ambos procesos (`cli2` y `serv2`) finalizan tras una única interacción, como exige el enunciado.
- Se han simulado los nombres de procesos con prints informativos (no visibles en `ps` como en Linux).

---

## Requisitos del sistema
- Python 3.7 o superior
- Sistema operativo: Windows

---

## Autora
Inés

---

¡Gracias por revisar la práctica! 🎓