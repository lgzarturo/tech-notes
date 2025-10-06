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

### Crear un entorno con `pipenv`

**Problema:**

Es necesario crear un entorno virtual para aislar las dependencias del proyecto. Es una buena práctica para evitar conflictos entre paquetes y versiones.

**Solución:**

Buscar las versiones de Python instaladas en el sistema:

```bash
py --list
```

Puedes crear un entorno virtual usando `pipenv` con el siguiente comando:

```bash
pipenv --python 3.8
pipenv install
```

o con windows:

```bash
pipenv --python "C:\Path\To\Python\python.exe"
pipenv install
```

Esto generará un archivo `Pipfile` en el directorio actual si no existe.

**Notas:**

- Asegúrate de tener `pipenv` instalado. Si no lo tienes, puedes instalarlo con `pip install pipenv`.
- Puedes especificar la versión de Python que deseas usar con el flag `--python`.
- Usa `pipenv install` para instalar las dependencias listadas en el `Pipfile`.

**Tags:** #pipenv #entorno_virtual #desarrollo

---

### Corregir un pipenv en un proyecto existente

**Problema:**

En Windows 11, al intentar activar el entorno virtual con `pipenv shell`, aparece el error:

```powershell
No module named pipenv
```

**Solución:**

Script para corregir el problema:

```powershell
<#
.SYNOPSIS
  Script para reparar la instalación de pipenv en Windows 11.

.DESCRIPTION
  - Detecta versiones de Python instaladas.
  - Verifica si pipenv está instalado y en el PATH.
  - Instala o reinstala pipenv en la versión activa de Python.
  - Corrige el PATH del usuario si falta la carpeta Scripts.
  - Valida la instalación final.
#>

Write-Host "🔧 Iniciando reparación de pipenv..." -ForegroundColor Cyan

# 1. Detectar versiones de Python disponibles
$pythonVersions = & py -0p 2>$null
if (-not $pythonVersions) {
    Write-Host "❌ No se encontraron versiones de Python instaladas." -ForegroundColor Red
    exit 1
}

Write-Host "`n📦 Versiones de Python detectadas:"
Write-Host $pythonVersions

# 2. Determinar versión activa de Python
$pythonPath = (Get-Command python).Source
$pythonVersion = & python --version
Write-Host "`n✅ Python activo: $pythonVersion ($pythonPath)"

# 3. Verificar si pipenv está instalado para esa versión
Write-Host "`n🔍 Verificando instalación de pipenv..."
$pipenvCheck = & python -m pip show pipenv 2>$null

if (-not $pipenvCheck) {
    Write-Host "⚙️  Instalando pipenv para $pythonVersion..." -ForegroundColor Yellow
    & python -m pip install --force-reinstall pipenv
} else {
    Write-Host "✅ pipenv ya está instalado." -ForegroundColor Green
}

# 4. Verificar carpeta Scripts en el PATH
$userScriptsPath = "$env:APPDATA\Python\" + $pythonVersion.Split(" ")[1] + "\Scripts"
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")

if ($currentPath -notmatch [regex]::Escape($userScriptsPath)) {
    Write-Host "`n🧭 Agregando Scripts al PATH del usuario..." -ForegroundColor Yellow
    [Environment]::SetEnvironmentVariable("Path", "$currentPath;$userScriptsPath", "User")
    Write-Host "✅ PATH actualizado. (Cierra y vuelve a abrir PowerShell)" -ForegroundColor Green
} else {
    Write-Host "✅ PATH correcto." -ForegroundColor Green
}

# 5. Validar ejecución de pipenv
Write-Host "`n🔎 Validando instalación..."
try {
    $version = & python -m pipenv --version
    Write-Host "✅ pipenv funcionando: $version" -ForegroundColor Green
} catch {
    Write-Host "❌ pipenv aún no responde correctamente." -ForegroundColor Red
    Write-Host "Puedes intentar ejecutar manualmente: py -3.12 -m pip install --user pipenv"
}

Write-Host "`n🎉 Proceso finalizado."
```

**Ejemplo:**

1. Guarda el script en un archivo llamado `fix_pipenv.ps1`.
2. Abre PowerShell como administrador.
3. Si es la primera vez que ejecutas un script, permite la ejecución con:

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   ```

4. Ejecuta el script:

   ```powershell
   .\fix_pipenv.ps1
   ```

5. Cuando termine, cierra y vuelve a abrir PowerShell para que los cambios en el PATH surtan efecto.
6. Intenta activar el entorno virtual nuevamente con:

   ```powershell
   pipenv --version
   pipenv --python <version python>
   pipenv shell
   ```

**Notas:**

- Asegúrate de tener permisos de administrador para modificar el PATH del usuario.
- El script detecta la versión activa de Python y asegura que `pipenv` esté instalado
- Corrige el PATH del usuario si la carpeta `Scripts` falta.
- Valida la instalación final de `pipenv`.

**Tags:** #pipenv #fix #windows11 #entorno_virtual

---
