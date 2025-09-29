# PostgreSQL

## Validar el número de conexiones actuales

### Problema

Necesito saber cuántas conexiones activas hay en mi base de datos PostgreSQL para monitorear el uso y evitar alcanzar el límite máximo de conexiones permitidas.

### Solución

- **Opción 1**: Consultar los parámetros de configuración para ver el límite máximo de conexiones permitidas.

```sql
-- Ver el límite máximo de conexiones permitidas
SHOW max_connections;

-- Ver las conexiones reservadas para superusuarios
SHOW superuser_reserved_connections;
```

- **Opción 2**: Consultar la vista del sistema `pg_stat_activity` para contar las conexiones activas actuales.

```sql
SELECT COUNT(*) FROM pg_stat_activity;
```

- **Opción 3**: Calcular las conexiones disponibles restando las conexiones activas del límite máximo.

```sql
SELECT
    (SELECT setting::int FROM pg_settings WHERE name = 'max_connections') 
    - count(*) 
    - (SELECT setting::int FROM pg_settings WHERE name = 'superuser_reserved_connections') 
    AS conexiones_disponibles
FROM pg_stat_activity;
```

- **Opción 4**: Ver el detalle por base de datos.

```sql
SELECT datname, COUNT(*) AS conexiones_activas
FROM pg_stat_activity
GROUP BY datname;
ORDER BY conexiones_activas DESC;
```

- **Opción 5**: Ver el detalle por usuario.

```sql
SELECT usename, COUNT(*) AS conexiones_activas
FROM pg_stat_activity
GROUP BY usename;
ORDER BY conexiones_activas DESC;
```

### Notas

Con estos comandos puedes monitorear el uso de conexiones en tu base de datos PostgreSQL y tomar medidas si te acercas al límite máximo. Si necesitas aumentar el límite, puedes modificar el parámetro `max_connections` en el archivo de configuración `postgresql.conf` y reiniciar el servidor.

**Objetivos**:

- Saber el limite máximo de conexiones.
- Saber cuántas conexiones activas hay.
- Saber cuántas conexiones disponibles hay.
- Ver el detalle de conexiones por base de datos.
- Ver el detalle de conexiones por usuario.

**Tags**: #postgresql #database #connections #monitoring

---

## Aumentar el límite de conexiones máximas

### Problema

Puede llegar a suceder el error: `FATAL: sorry, too many clients already` cuando se alcanzan el número máximo de conexiones permitidas en PostgreSQL. Para evitar este error, es necesario aumentar el límite de conexiones máximas.

### Solución

- **Opción 1**: Aumentar max_connections en el archivo de configuración `postgresql.conf`.

```bash
# Ejemplo de comando para aumentar max_connections
echo "max_connections = 200" >> /etc/postgresql/12/main/postgresql.conf
```

> Si estás usando docker, no se necesita hacer un build de la imagen, solo reiniciar el contenedor. A menos que el archivo postgresql.conf esté empaquetado en la imagen y no como volumen.

```bash
docker restart <nombre_del_contenedor>
```

- **Opción 2**: Verificar los recursos del sistema para asegurarse de que puede manejar más conexiones.

```bash
# Verificar el límite de archivos abiertos
ulimit -n
```

- Mas conexiones requieren más memoria y CPU. Asegúrate de que tu sistema tenga suficientes recursos para manejar el aumento. Cada conexión consume memoria adicional, no solo work_mem, sino también otros buffers y estructuras internas.
- No es buena práctica establecer un valor extremadamente alto para `max_connections` sin considerar los recursos del sistema.

Entornos productivos:

- Mantener `max_connections` entre 100 y 200.
- Usar un pool de conexiones como PgBouncer o Pgpool-II para manejar muchas conexiones de manera eficiente.

> Aumentar de 100 a 300 conexiones no debería ser un problema en la mayoría de los sistemas modernos, pero siempre es bueno verificar.

- **Opción 3**: Liberar conexiones activas innecesarias.

```sql
-- Ver el conteo de conexiones por usuario, base de datos y estado
SELECT usename, datname, state, count(*) 
FROM pg_stat_activity 
GROUP BY usename, datname, state
ORDER BY count(*) DESC;

-- Ver conexiones activas
SELECT pid, usename, datname, client_addr, state, query
FROM pg_stat_activity;

-- Terminar una conexión específica (reemplaza <pid> con el ID del proceso)
SELECT pg_terminate_backend(<pid>);
```

> Si ves muchas conexiones en estado `idle`, podrías considerar ajustar el tiempo de espera para conexiones inactivas usando el parámetro `idle_in_transaction_session_timeout` en `postgresql.conf`. Antes de eso, investiga por qué las conexiones están quedando inactivas, hay que validar el cierre correcto en la aplicación, validar que haya un pool de conexiones (ej. HikariCP en SpringBoot con maxLifetime y idleTimeout configurados).

### Notas

Aumentar el límite de conexiones máximas puede ayudar a evitar errores relacionados con demasiadas conexiones, pero es importante hacerlo de manera responsable y considerar el impacto en los recursos del sistema. Siempre monitorea el uso de conexiones y ajusta según sea necesario.

- Si solo es para dev/test: aumentar a 200 o 300 conexiones no debería ser un problema.
- En producción: no subas tanto el límite sin antes considerar un pool de conexiones, hay que evitar la saturación del servidor.

**Tags**: #postgresql #database #connections #max_connections #configuration

---
