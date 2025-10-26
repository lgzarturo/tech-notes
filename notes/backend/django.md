---
title: Django
tags: [backend, python, django, development]
category: backend
status: draft
created: 2025-10-26
updated: 2025-10-26
related: []
---

## Django

Django es un framework web de alto nivel para Python que fomenta el desarrollo rápido y limpio. Está diseñado para ayudar a los desarrolladores a crear aplicaciones web de manera eficiente, siguiendo el principio de "no te repitas" (DRY, por sus siglas en inglés). Django incluye una serie de características integradas, como un sistema de administración automático, un ORM (Object-Relational Mapping) potente, y soporte para autenticación de usuarios, entre otras. Su arquitectura basada en el patrón Modelo-Vista-Controlador (MVC) facilita la separación de preocupaciones y la escalabilidad de las aplicaciones web.

---

### Configuración de logging en Django

**Problema:**

El objetivo es configurar el sistema de logging en Django para registrar eventos importantes, errores y advertencias durante la ejecución de la aplicación.

**Solución:**

Instalar el módulo de logging de Python y configurar el archivo `settings.py` de Django para definir los manejadores, formateadores y niveles de logging.

```bash
pip install logging
```

En `settings.py`, agregar la configuración de logging:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

> Este código configura un manejador de archivos que registra mensajes de nivel ERROR en un archivo llamado `django.log`.

**Ejemplos:**

Ahora importar y usar el módulo de logging en tus vistas o cualquier otro lugar de tu aplicación Django:

```python
import logging
```

Usar el logger para registrar mensajes:

```python
logger = logging.getLogger('django')
logger.error('Este es un mensaje de error')
```

Usar el logger para registrar mensajes en diferentes niveles:

```python
logger.debug('Mensaje de depuración')
logger.info('Mensaje informativo')
logger.warning('Mensaje de advertencia')
logger.error('Mensaje de error')
logger.critical('Mensaje crítico')
```

Usar el logger en vistas de Django:

```python
from django.http import HttpResponse
import logging

logger = logging.getLogger('django')

def my_view(request):
    logger.info('Se ha accedido a la vista my_view')
    return HttpResponse('Hola, mundo!')
```

Usar el logger en middleware personalizado:

```python
from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger('django')

class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.info(f'Request URL: {request.path}')
```

Usar el logger para registrar excepciones:

```python
try:
    # Código que puede generar una excepción
except Exception as e:
    logging.exception(str(e))
```

Usar el logger para signals:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging

logger = logging.getLogger('django')

from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def log_model_save(sender, instance, created, **kwargs):
    if created:
        logger.info(f'Nuevo objeto creado: {instance}')
    else:
        logger.info(f'Objeto actualizado: {instance}')
```

**Notas:**

Puedes personalizar aún más la configuración de logging según tus necesidades, como agregar más manejadores (por ejemplo, para enviar logs a la consola o a un servicio externo), cambiar los niveles de logging, o definir formateadores personalizados para los mensajes de log.

Es importante revisar regularmente los archivos de log para identificar y solucionar problemas en tu aplicación Django.

**Tags:** #logging #django #python #backend

---
