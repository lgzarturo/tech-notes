# Python

## Instalar dependencias de desarrollo con pipenv

### Problema
Configurar un entorno de desarrollo con todas las dependencias necesarias.

### Solución

```bash
# Crear un nuevo entorno virtual
pipenv --python 3.8

# Instalar dependencias
pipenv install flask sqlalchemy

# Activar el entorno virtual
pipenv shell
```

### Notas

Instalar dependencia de desarrollo, es decir, que solo se usará en el entorno de desarrollo:

- Usa `Pipfile` para gestionar dependencias.
- Usa `Pipfile.lock` para versiones específicas.

**Tags:** #pipenv #entorno_virtual #desarrollo

---
