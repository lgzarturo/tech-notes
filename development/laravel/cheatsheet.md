# Cheatsheet — comandos y ajustes clave (Windows, PHP via winget, Laravel)

Resumen práctico de referencia rápida para configurar PHP, habilitar extensiones y resolver incidencias comunes en Laravel.

---

## Comprobación de PHP y `php.ini`

```powershell
# Mostrar qué php.ini carga la CLI
php --ini

# Ver versión de PHP
php -v

# Mostrar todas las configuraciones (salida larga)
php -i

# Buscar una configuración concreta (PowerShell)
php -i | Select-String memory_limit
php -i | Select-String max_execution_time

# Mostrar módulos cargados
php -m

# Buscar si aparece un módulo concreto
php -m | Select-String fileinfo
php -m | Select-String sqlite
```

* `php --ini` indica la ruta de **Loaded Configuration File**: ese es el `php.ini` que debes editar para la CLI (y para `php artisan`).
* Si modificas `php.ini`, la CLI lo recoge inmediatamente. Si usas un servidor web (Apache, Nginx, PHP-FPM), reinícialo para aplicar cambios.

---

## Crear / validar phpinfo

Archivo `phpinfo.php`:

```php
<?php
phpinfo();
```

* Ejecuta en terminal: `php phpinfo.php` para ver configuración CLI.
* En un servidor web, colócalo en `public/` y ábrelo en el navegador para ver la configuración del PHP que usa el servidor web.

---

## Habilitar extensiones en `php.ini` (Windows)

Busca las líneas correspondientes y **quita el `;`** para activar:

```ini
; ejemplos de líneas a activar
extension=fileinfo
extension=curl
extension=mbstring
extension=openssl
extension=pdo_sqlite
extension=sqlite3
extension=pdo_mysql     ; si usas MySQL
extension=pdo_pgsql     ; si usas PostgreSQL
extension=xml           ; xmlreader/xmlwriter según la distro
extension=bcmath
extension=gd
```

* Recomendado mínimo para Laravel 12: `curl`, `fileinfo`, `mbstring`, `openssl`, `pdo` (o drivers específicos pdo_mysql/pdo_sqlite/pdo_pgsql), `xml`, `tokenizer`, `ctype`.
* Verifica `extension_dir` (ruta donde están los DLLs) con:

  ```powershell
  php -i | Select-String extension_dir
  ```

* Confirma presencia del DLL en `ext` si una extensión no carga.

---

## Solución al error `Install or enable PHP's fileinfo extension`

* Si Composer falla por `ext-fileinfo`:

  1. Edita el `php.ini` que muestra `php --ini`.
  2. Añade o descomenta: `extension=fileinfo` o `extension=php_fileinfo.dll`.
  3. Guarda y verifica con `php -m | Select-String fileinfo`.
  4. Comando temporal (no recomendable para producción):

     ```bash
     composer create-project laravel/laravel nombre --ignore-platform-req=ext-fileinfo
     ```

---

## Solución al error `could not find driver (Connection: sqlite)`

* Habilita en `php.ini`:

```ini
extension=pdo_sqlite
extension=sqlite3
```

* Crea el archivo SQLite si no existe:

```powershell
# desde PowerShell (en la raíz del proyecto)
New-Item -Path .\database\database.sqlite -ItemType File

# o desde CMD
type nul > database\database.sqlite
```

* Asegura permisos de lectura/escritura en `database/database.sqlite`.
* Verifica con: `php -m | Select-String sqlite` y con `php phpinfo.php` que PDO drivers incluya `sqlite`.

---

## Comandos Laravel / Composer usados en la conversa

```bash
# Instalar un proyecto Laravel (última versión por defecto)
laravel new proyecto

# Instalar Laravel versión 11 (ejemplo)
composer create-project laravel/laravel:^11.* nombre-de-proyecto

# Alternativa para especificar versión (otro formato)
composer create-project "laravel/laravel:^11.0" nombre-de-proyecto

# Generar key y preparar .env
copy .env.example .env          # Windows CMD
cp .env.example .env            # PowerShell / bash
php artisan key:generate

# Ejecutar servidor local
php artisan serve

# Migrar BD
php artisan migrate
```

* `laravel new` suele instalar la versión más reciente del installer. Para una versión específica, usa `composer create-project` con la versión deseada.
* Si Composer falla por extensiones PHP, primero habilita las extensiones y luego reintenta.

---

## Ver y ajustar `memory_limit` y `max_execution_time`

* Búsqueda directa en PowerShell:

```powershell
php -i | Select-String memory_limit
php -i | Select-String max_execution_time
```

* Obtener valores desde PHP:

```bash
php -r "echo 'memory_limit: '.ini_get('memory_limit').PHP_EOL; echo 'max_execution_time: '.ini_get('max_execution_time').PHP_EOL;"
```

* Para cambiar, edita el `php.ini`:

```ini
memory_limit = 512M
max_execution_time = 120
```

* Nota: en CLI `max_execution_time` suele ser `0` (sin límite); aplica sobre todo al servidor web o a scripts cron si los necesitas limitar.

---

## Checklist rápido de resolución de incidencias (orden práctico)

1. `php --ini` → identifica `php.ini` correcto.
2. Edita `php.ini` como administrador.
3. Habilita extensiones necesarias (`fileinfo`, `mbstring`, `pdo_sqlite`, `pdo_mysql`, `openssl`, `curl`, `xml`, etc).
4. Verifica módulos cargados: `php -m`.
5. Crea/asegura `database/database.sqlite` si usas SQLite.
6. Reinicia servidor web (si aplica).
7. Reintenta `composer create-project` / `php artisan migrate`.
8. Si Composer sigue fallando por requisitos de plataforma, usa temporalmente `--ignore-platform-req=...` solo para debug.

---

## Notas finales y buenas prácticas

* Si tienes múltiples instalaciones de PHP en Windows, asegúrate que la ruta en PATH y el `php --ini` correspondan a la instalación que quieres modificar.
* Para desarrollo local usa `php.ini-development` como base; renómbralo a `php.ini` si no existe. Para producción usa `php.ini-production`.
* No ignores permanentemente requisitos de extensiones con Composer; mejor habilita la extensión correcta en `php.ini`.

---

## 🧰 Archivo: `Check-LaravelEnv.ps1`

**Script PowerShell** que valida si el entorno está listo para ejecutar **Laravel (v11 o v12)**, comprobando que PHP, Composer y las extensiones necesarias estén instaladas y configuradas correctamente.

---

```powershell
<#
.SYNOPSIS
  Valida entorno PHP y Composer para proyectos Laravel.
.DESCRIPTION
  Verifica versiones, configuración y extensiones requeridas.
  Ideal para diagnóstico antes de instalar o correr Laravel.
#>

Write-Host "=== Verificación del entorno para Laravel ===`n" -ForegroundColor Cyan

# --- PHP ---
if (Get-Command php -ErrorAction SilentlyContinue) {
    $phpVersion = php -v | Select-String "PHP"
    Write-Host "✔ PHP encontrado: $phpVersion" -ForegroundColor Green

    # php.ini
    $phpIni = (php --ini | Select-String "Loaded Configuration File").ToString().Split(":")[-1].Trim()
    Write-Host "Archivo php.ini cargado:`n  $phpIni`n"

    # extension_dir
    $extDir = php -i | Select-String "extension_dir" | ForEach-Object { $_.ToString().Split("=>")[-1].Trim() } | Select-Object -First 1
    Write-Host "Directorio de extensiones:`n  $extDir`n"

    # Extensiones requeridas
    $requiredExtensions = @("fileinfo", "curl", "mbstring", "openssl", "pdo_sqlite", "pdo_mysql", "xml", "bcmath", "ctype", "tokenizer")
    $loadedExtensions = php -m
    $missingExtensions = @()

    foreach ($ext in $requiredExtensions) {
        if ($loadedExtensions -match $ext) {
            Write-Host "✔ Extensión activa: $ext" -ForegroundColor Green
        } else {
            Write-Host "✖ Falta extensión: $ext" -ForegroundColor Yellow
            $missingExtensions += $ext
        }
    }

    # memory_limit y max_execution_time
    Write-Host "`nConfiguraciones importantes:`n" -ForegroundColor Cyan
    php -r "echo 'memory_limit: '.ini_get('memory_limit').PHP_EOL;"
    php -r "echo 'max_execution_time: '.ini_get('max_execution_time').PHP_EOL;"

} else {
    Write-Host "✖ PHP no encontrado en PATH. Instálalo con winget:" -ForegroundColor Red
    Write-Host "  winget install --id=PHP.PHP -e"
    exit 1
}

# --- Composer ---
Write-Host "`n--- Composer ---" -ForegroundColor Cyan
if (Get-Command composer -ErrorAction SilentlyContinue) {
    $composerVersion = composer --version
    Write-Host "✔ Composer encontrado: $composerVersion" -ForegroundColor Green

    # Probar diagnóstico de composer
    Write-Host "`nEjecutando composer diagnose..." -ForegroundColor Cyan
    composer diagnose
} else {
    Write-Host "✖ Composer no encontrado. Instálalo con winget:" -ForegroundColor Red
    Write-Host "  winget install --id=Composer.Composer -e"
    exit 1
}

# --- Laravel Installer ---
Write-Host "`n--- Laravel Installer ---" -ForegroundColor Cyan
$laravelInstaller = Get-Command laravel -ErrorAction SilentlyContinue
if ($laravelInstaller) {
    $laravelVersion = laravel --version
    Write-Host "✔ Laravel Installer disponible: $laravelVersion" -ForegroundColor Green
} else {
    Write-Host "✖ Laravel Installer no encontrado." -ForegroundColor Yellow
    Write-Host "  Puedes instalarlo con: composer global require laravel/installer`n"
}

# --- Resumen final ---
Write-Host "`n=== Resumen ===" -ForegroundColor Cyan
if ($missingExtensions.Count -eq 0) {
    Write-Host "✅ Todo correcto. El entorno está listo para Laravel." -ForegroundColor Green
} else {
    Write-Host "⚠ Faltan extensiones: $($missingExtensions -join ', ')" -ForegroundColor Yellow
    Write-Host "Edita el archivo php.ini en:`n  $phpIni`npara habilitarlas (quita el ';' en cada línea correspondiente)." -ForegroundColor Yellow
}

Write-Host "`n--- Fin del diagnóstico ---" -ForegroundColor Cyan
```

---

## 💡 Cómo usarlo

1. Guarda el contenido como `Check-LaravelEnv.ps1` en tu carpeta de proyectos o utilidades.
2. Abre PowerShell **como administrador**.
3. Si no tienes habilitados scripts locales:

   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. Ejecuta el script:

   ```powershell
   .\Check-LaravelEnv.ps1
   ```

---

## 🔍 Qué valida el script

* Detecta si PHP está instalado y en el PATH.
* Muestra la versión y el `php.ini` activo.
* Muestra la ruta de `extension_dir`.
* Comprueba las extensiones clave para Laravel (`fileinfo`, `curl`, `mbstring`, `pdo_sqlite`, etc.).
* Informa del `memory_limit` y `max_execution_time`.
* Comprueba Composer y su diagnóstico (`composer diagnose`).
* Verifica si tienes el instalador global de Laravel.
