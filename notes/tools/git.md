---
title: Git
tags: [tools, git, version-control, daily]
category: tools
status: draft
created: 2025-10-05
updated: 2025-10-05
related: [[notes/daily/git-commands.md]]
---

## Git

Git es un sistema de control de versiones distribuido que permite a los desarrolladores rastrear cambios en el código fuente a lo largo del tiempo. Es ampliamente utilizado en el desarrollo de software para facilitar la colaboración entre equipos y la gestión de proyectos.

---

### Conventional commits vscode

**Problema:**

El objetivo es estandarizar los mensajes de commit para mejorar la legibilidad y facilitar la generación automática de changelogs. Y que los mensajes de commit sigan una convención específica, usando un formato predefinido, como "feat:", "fix:", "docs:", etc. Esto ayuda a que chat copilot entienda mejor el contexto de los cambios realizados y sugiera mensajes de commit más precisos y relevantes.

**Solución:**

Generar un archivo en `.github/` llamado `.conventional-commits.md` con el siguiente contenido:

```markdown
# Instrucciones para mensajes de commit en español usando Conventional Commits v1.0.0

- Genera el mensaje de commit completamente en español.  
- Usa la estructura: `tipo(scope): descripción breve`, donde:
  - `tipo` debe ser *feat, fix, docs, style, refactor, test, chore, ci o perf*. "usa el tipo adecuado según el cambio realizado".  
  - Si hay scope, debe indicarse entre paréntesis, en minúsculas: `feat(api): ...`
- El título (primer renglón) **no debe exceder 72 caracteres**, sin punto final.  
- Título en minúsculas, salvo acrónimos o nombres propios (`API`, `Next.js`).  
- La descripción debe estar en **modo imperativo** (“agrega”, “corrige”, “refactoriza”), no en pasado.  
- Si hay cuerpo (body):
  - Colócalo después de una línea en blanco.
  - Organiza puntos con viñetas cortas: 
    - ¿Qué cambia?  
    - ¿Por qué?
  - Cada línea del body también debe tener hasta 72 caracteres.
- Si aplica:
  - Incluye sección de *footer* con `BREAKING CHANGE:` o referencia tipo `ISSUE‑123`.
- No pongas punto final en el título.  
- Toda la información relevante debe quedar en el body o footer si no cabe en el título.

**Ejemplo en español:**

feat(db): agrega endpoint para creación de producto

- crea vista de Drizzle ORM en product.schema.ts
- añade lógica en API route /api/productos
- valida los campos requeridos antes de inserción

fix(ui): corrige clase Tailwind errónea en formulario

- cambia bg-grey-200 por bg-gray-200
- se visualiza correctamente el botón enviar
```

Modifica la configuración de VSCode `.vscode/settings.json` para usar este archivo como referencia al generar mensajes de commit:

```jsonc
{
  "github.copilot.chat.commitMessageGeneration.instructions": [
    {
      "file": ".github/.conventional-commits.md"
    }
  ],
  "github.copilot.chat.localeOverride": "es"
}
```

**Notas:**

- La instrucción "file": "{{ruta}}" le indica a Copilot que utilice este archivo personalizado como guía al generar mensajes de commit.
- El ajuste "localeOverride": "es" fuerza la generación en español, independientemente del idioma del IDE o ubicación del usuario.

> Cada vez que uses Copilot para generar commits, haz una revisión rápida del mensaje (especialmente scope y longitud).

**Tags:** #tools #git #conventional_commits #vscode #copilot

---
