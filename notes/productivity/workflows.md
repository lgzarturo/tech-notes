# Workflows

## Eliminar un pueto en uso

### Problema
El servidor no puede iniciarse porque el puerto ya está en uso.

### Solución

- **MacOS / Linux**: Usa los siguientes comandos en la terminal para encontrar y matar el proceso que está usando el puerto.

```bash
# Encuentra el proceso que está usando el puerto
lsof -i :<puerto>

# ó para obtener el PID del proceso (la segunda columna en la salida del comando anterior)
sudo lsof -nP -iTCP:4444 -sTCP:LISTEN

# Mata el proceso (reemplaza <PID> con el ID del proceso encontrado)
kill -9 <PID>
```

- **Windows**: Usa los siguientes comandos en el símbolo del sistema (cmd/PowerShell) para encontrar y matar el proceso que está usando el puerto.

```cmd
# Encuentra el PID del proceso que está usando el puerto
netstat -ano | findstr :<puerto>

# Mata el proceso (reemplaza <PID> con el ID del proceso encontrado)
taskkill /PID <PID> /F
```

### Notas

Si ese puerto lo usabas para autossh o un túnel SSH, asegúrate de cerrarlo antes de volver a levantarlo de nuevo, ya que podría generar conflictos o quedarse colgado en segundo plano.

---