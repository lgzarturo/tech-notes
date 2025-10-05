---
title: IntelliJ
tags: [tools, intellij, java, performance]
category: tools
status: draft
created: 2025-10-05
updated: 2025-10-05
related: []
---

## IntelliJ IDEA

IntelliJ IDEA es un entorno de desarrollo integrado (**IDE**) para Java y otros lenguajes de programación. Es conocido por su potente soporte para el desarrollo de aplicaciones, incluyendo características como autocompletado de código, refactorización, depuración y herramientas de integración con sistemas de control de versiones.

---

### Evitar que IntelliJ consuma mucha memoria

**Problema:**

IntelliJ IDEA puede consumir mucha memoria RAM, lo que puede ralentizar tu computadora, en especial si tienes varios proyectos abiertos o si tu computadora tiene recursos limitados.

**Solución:**

1. Limitar recursos de la JVM en tus ejecuciones

   Cuando corres una app desde IntelliJ, se lanza con parámetros de la JVM.
   Puedes controlar memoria máxima y número de hilos:
   - Abre el menú Run → Edit Configurations.
   - En tu configuración de ejecución agrega en VM options algo como:

   ```bash
   -Xmx1024m -Xms512m -XX:CICompilerCount=2
   ```

   - `-Xmx1024m` → máximo 1GB de RAM.
   - `-Xms512m` → mínimo 512MB de RAM.
   - `-XX:CICompilerCount=2` → limita compiladores JIT a 2 hilos (evita que use todos los núcleos).

   > Así evitas que se coma toda la RAM y CPU.

2. Limitar IntelliJ IDEA en sí

   IntelliJ también es pesado y puede disparar el uso de CPU (indexación, análisis, etc.).

   - Edita el archivo de configuración de IntelliJ según tu sistema:
     - Windows: idea64.exe.vmoptions (en `C:\Program Files\JetBrains\IntelliJ IDEA [versión]\bin\`)
     - O desde el menú: Help → Edit Custom VM Options…

   Ejemplo de límites razonables:

   ```properties
   -Xms512m
   -Xmx2048m
   -XX:MaxPermSize=512m
   -XX:ReservedCodeCacheSize=512m
   ```

3. Bajar la prioridad de los procesos Java

   Si quieres que Java no bloquee tu PC aunque use CPU:

   - Abre Administrador de tareas → pestaña Detalles.
   - Clic derecho en java.exe o idea64.exe → Establecer prioridad → ponlo en Baja.

   O automático con PowerShell:

   ```powershell
   Get-Process java | ForEach-Object { $_.PriorityClass = 'BelowNormal' }
   ```

**Notas:**

Esto ayuda a que IntelliJ y tus apps Java no consuman toda la memoria y CPU, manteniendo tu PC más fluida.

**Tags:** #performance #java #intellij

---
