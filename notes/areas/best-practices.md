---
title: Best Practices
tags: [areas, best-practices, coding-standards]
category: areas
status: draft
created: 2025-10-22
updated: 2025-10-22
related: []
---

## Best Practices

Algunas de las mejores prácticas en el desarrollo de software incluyen:

- **Escribir código limpio y legible:** Utiliza nombres de variables y funciones descriptivos, y sigue un estilo de codificación consistente.
- **Documentar el código:** Incluye comentarios y documentación para explicar la lógica y el propósito del código.
- **Realizar pruebas:** Implementa pruebas unitarias y de integración para asegurar la calidad del código y detectar errores temprano.
- **Usar control de versiones:** Utiliza herramientas como Git para rastrear cambios en el código y colaborar con otros desarrolladores.
- **Seguir principios de diseño:** Aplica principios como SOLID y DRY para crear un código más mantenible y escalable.

---

### Métodos API RESTful

**Problema:**

Muchas veces no está claro qué métodos HTTP utilizar para diferentes operaciones en una API RESTful.
Esto puede llevar a inconsistencias y dificultades para los consumidores de la API. Lo ideal es seguir las convenciones establecidas para mejorar la claridad y la interoperabilidad.

**Solución:**

Implementar una REST API bien estructurada implica seguir buenas prácticas que faciliten su uso, mantenimiento y escalabilidad. A continuación te comparto las **mejores prácticas**, con especial enfoque en:

1. **Uso adecuado de métodos HTTP**
2. **Convenciones para nombrar endpoints**
3. **Estructura general y manejo de respuestas**

**Métodos HTTP: Cuándo y cómo usarlos**

| Método     | Uso común                            | Idempotente | Ejemplo             |
| ---------- | ------------------------------------ | ----------- | ------------------- |
| **GET**    | Obtener recursos (solo lectura)      | ✅           | `GET /users/123`    |
| **POST**   | Crear un recurso nuevo               | ❌           | `POST /users`       |
| **PUT**    | Reemplazar un recurso (update total) | ✅           | `PUT /users/123`    |
| **PATCH**  | Actualización parcial                | ✅           | `PATCH /users/123`  |
| **DELETE** | Eliminar un recurso                  | ✅           | `DELETE /users/123` |

> ⚠️ **Idempotente**: puedes hacer la misma petición varias veces y el resultado será el mismo (no se crean duplicados, por ejemplo).

---

**Convenciones para nombrar endpoints**

Reglas generales

- Usar **nombres en plural**: `/users`, `/products`
- Usar **nombres basados en recursos** (no en acciones): `/users` ✅ en lugar de `/getUser` ❌
- Jerarquía lógica: `/users/123/orders/456`
- No incluir verbos: usa el método HTTP para definir la acción
- Usa **kebab-case** o **snake_case** si necesitas separar palabras, pero **camelCase** no es común en REST

**Ejemplos**

| Acción                       | Endpoint      | Método   |
| ---------------------------- | ------------- | -------- |
| Obtener todos los usuarios   | `/users`      | `GET`    |
| Obtener usuario por ID       | `/users/{id}` | `GET`    |
| Crear usuario                | `/users`      | `POST`   |
| Actualizar usuario (total)   | `/users/{id}` | `PUT`    |
| Actualizar usuario (parcial) | `/users/{id}` | `PATCH`  |
| Eliminar usuario             | `/users/{id}` | `DELETE` |

**Estructura de rutas**

- **Anidación solo si el recurso depende del padre**:

  - `GET /users/123/orders` (porque las órdenes pertenecen a un usuario)
  - Evita anidación profunda como `/users/123/orders/456/items/789/comments/999` ❌

**Paginación, filtros y ordenamiento**

Usa **query params** para esto:

```http
GET /products?category=shoes&page=2&limit=20&sort=price_desc
```

**Estándar de respuestas**

- Código HTTP correcto:

  - `200 OK`, `201 Created`, `204 No Content`, `400 Bad Request`, `404 Not Found`, `500 Internal Server Error`
- Incluye mensajes claros y datos útiles en el body JSON:

```json
{
  "message": "User not found",
  "code": 404
}
```

**Formato consistente (por ejemplo, JSON)**

```json
{
  "id": 123,
  "name": "Arturo",
  "email": "arturo@example.com"
}
```

**Manejo de errores**

Devuelve errores con estructura uniforme:

```json
{
  "error": "Invalid input",
  "details": [
    { "field": "email", "message": "Email is required" }
  ]
}
```

**Versionado de la API**

- Coloca la versión en la URL si lo necesitas:

  - `/api/v1/users`
- O mejor aún: en el header:

  - `Accept: application/vnd.company.v1+json`

**Notas:**

- Estas prácticas ayudan a crear APIs RESTful claras, consistentes y fáciles de usar.
- Adapta estas recomendaciones según las necesidades específicas de tu proyecto y equipo.
- Mantente actualizado con las mejores prácticas y estándares de la industria.

**Tags:** #best-practices #api #rest #http

---
