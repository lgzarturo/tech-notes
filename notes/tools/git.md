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

### ¿Como dar commit a un tag?

**Problema:**

Quiero crear un commit asociado a un tag específico en Git para marcar una versión o hito importante en el historial del proyecto. Se usa comúnmente para versiones de lanzamiento (releases) o puntos clave en el desarrollo, son referencias útiles para identificar versiones específicas del código.

**Solución:**

Para crear un commit asociado a un tag en Git, sigue estos pasos:

1. Crea un nuevo tag (si aún no existe) usando el comando:

   ```bash
   git tag -a v1.0 -m "Versión 1.0"
   ```

2. Realiza cambios en tu código y haz un commit:

   ```bash
   git add .
   git commit -m "Descripción de los cambios"
   ```

3. Asocia el commit al tag usando el comando:

   ```bash
   git tag -f v1.0
   ```

4. Finalmente, sube el tag al repositorio remoto:

   ```bash
   git push origin v1.0
   ```

**Notas:**

- Reemplaza `v1.0` con el nombre del tag que deseas usar.
- El comando `-f` en `git tag -f` fuerza la actualización del tag al commit más reciente.
- Asegúrate de comunicar a tu equipo si estás sobrescribiendo un tag existente, ya que esto puede afectar a otros desarrolladores que dependan de ese tag.

**Tags:** #tools #git #tags #versioning

---

### Rollback de un commit

**Problema:**

Necesito revertir un commit específico en mi historial de Git debido a que introdujo errores o cambios no deseados en el código. Quiero asegurarme de que el historial del proyecto se mantenga limpio y que los cambios problemáticos sean eliminados de manera segura.

**Solución:**

Hay dos escenarios comunes para hacer rollback de un commit en Git:

Para hacer un rollback del commit `685bf37` y revertir los cambios aplicados en ese commit en tu repositorio Git, tienes varias opciones, dependiendo de lo que quieras lograr:

---

**Opción 1: Revertir el commit con `git revert`**

> RECOMENDADO si ya se hizo `push`

Esto crea un nuevo commit que **deshace los cambios** introducidos por el commit `685bf37`, sin alterar el historial.

```bash
git revert 685bf37
```

* Git abrirá tu editor para escribir el mensaje del commit de reversión.
* Puedes guardar y salir, o usar la opción `--no-edit` para evitarlo:

```bash
git revert 685bf37 --no-edit
```

Después:

```bash
git push origin <rama>
```

**Opción 2: Reset con `git reset`**

> Útil si NO has hecho `push` aún

Si el commit `685bf37` está solo localmente y **todavía no lo subes**, puedes hacer:

Para deshacer el commit y mantener los cambios en tu working directory (modo "soft"):

```bash
git reset --soft HEAD^
```

Para deshacer el commit y también los cambios del working directory (modo "hard"):

> ⚠️ **Esto borra los cambios de ese commit, sin posibilidad de recuperación** (a menos que los stashées o copies antes):

```bash
git reset --hard HEAD^
```

Después de hacer el reset:

```bash
git push origin <rama> --force
```

**¿Cuál usar?**

| Situación                                | Usa...             |
| ---------------------------------------- | ------------------ |
| Ya hiciste `push` al commit              | `git revert`       |
| No has hecho `push` y quieres eliminarlo | `git reset`        |
| No te importa borrar cambios             | `git reset --hard` |

**Notas:**

- Siempre revisa el historial con `git log` antes de hacer rollback.
- Considera comunicar a tu equipo si haces un `git reset --hard` y `push --force`, ya que puede afectar a otros desarrolladores.
- Si necesitas recuperar un commit eliminado, puedes usar `git reflog` para encontrar su referencia.

**Tags:** #tools #git #rollback #revert #reset

---
