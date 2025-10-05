---
title: Python
tags: [backend, python, pipenv, development]
category: backend
status: draft
created: 2025-10-05
updated: 2025-10-05
related: []
---

## Python

Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Es conocido por su legibilidad y simplicidad, lo que lo convierte en una excelente opción para principiantes y desarrolladores experimentados. Python cuenta con una amplia variedad de bibliotecas y frameworks que facilitan el desarrollo de aplicaciones en diferentes dominios, como web, ciencia de datos, inteligencia artificial y más.

---

### Instalar dependencias de desarrollo con pipenv

**Problema:**

Configurar un entorno de desarrollo con todas las dependencias necesarias.

**Solución:**

```bash
# Crear un nuevo entorno virtual
pipenv --python 3.8

# Instalar dependencias
pipenv install flask sqlalchemy

# Activar el entorno virtual
pipenv shell
```

**Notas:**

Instalar dependencia de desarrollo, es decir, que solo se usará en el entorno de desarrollo:

- Usa `Pipfile` para gestionar dependencias.
- Usa `Pipfile.lock` para versiones específicas.

**Tags:** #pipenv #entorno_virtual #desarrollo

---
