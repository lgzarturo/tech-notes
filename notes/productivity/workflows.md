# Workflows

## Eliminar un puerto en uso

### Problema
El servidor no puede iniciarse porque el puerto ya está en uso.

### Solución

- **MacOS / Linux**: Usa los siguientes comandos en la terminal para encontrar y matar el proceso que está usando el puerto.

```bash
# Encuentra el proceso que está usando el puerto
lsof -i :<puerto>

# ó para obtener el PID del proceso (la segunda columna en la salida del comando anterior)
sudo lsof -nP -iTCP:4444 -sTCP:LISTEN

# Mata el proceso (reemplaza <PID> con el ID del proceso encontrado)
kill -9 <PID>
```

- **Windows**: Usa los siguientes comandos en el símbolo del sistema (cmd/PowerShell) para encontrar y matar el proceso que está usando el puerto.

```cmd
# Encuentra el PID del proceso que está usando el puerto
netstat -ano | findstr :<puerto>

# Mata el proceso (reemplaza <PID> con el ID del proceso encontrado)
taskkill /PID <PID> /F
```

### Notas

Si ese puerto lo usabas para autossh o un túnel SSH, asegúrate de cerrarlo antes de volver a levantarlo de nuevo, ya que podría generar conflictos o quedarse colgado en segundo plano.

**Tags:** #workflow #port #killprocess #linux #macos #windows

---

## Eliminar procesos de java colgados por el IntelliJ

### Problema
A veces, los procesos de Java pueden quedar colgados y no cerrarse correctamente al detener una aplicación en IntelliJ, lo que puede causar problemas al intentar reiniciar la aplicación.

### Solución
1. Abre la terminal.
2. Ejecuta el siguiente comando para encontrar el PID de los procesos de Java en ejecución:

```bash
jps -l
```

3. Identifica el PID del proceso que deseas eliminar.
4. Mata el proceso usando el siguiente comando (reemplaza `<PID>` con el ID del proceso encontrado):

```bash
killall -9 java
```

> Esto matará todos los procesos de Java en ejecución, sin importar de que aplicación provengan.

4. Para solo matar los procesos de Java de IntelliJ, puedes usar:

```bash
ps -ef | grep "idea" | grep java | awk '{print $2}' | xargs kill -9
```

> Esto detecta solo los procesos de Java que contienen "idea" en su línea de comando, que es típico de los procesos iniciados por IntelliJ.

### Notas

Primero usa `jps -l` para ver los procesos de Java en ejecución y asegurarte de que estás matando el proceso correcto. Si tienes múltiples aplicaciones Java en ejecución, matar todos los procesos puede afectar otras aplicaciones.

**Tags:** #workflow #port #killprocess #linux #macos #java #intellij

---

## Matar procesos de Java colgados en Windows

### Problema

En Windows, los procesos de Java pueden quedar colgados y no cerrarse correctamente al detener una aplicación en IntelliJ, lo que puede causar problemas al intentar reiniciar la aplicación.

### Solución

En Windows, cuando cierras IntelliJ IDEA a veces los procesos de Java (JDK) que ejecutaban tu aplicación o tests se quedan colgados en segundo plano. Para matarlos puedes hacerlo de varias formas:

1. Desde el Administrador de Tareas
	1.	Presiona Ctrl + Shift + Esc.
	2.	Ve a la pestaña Detalles.
	3.	Ordena por Nombre y busca java.exe o javaw.exe.
	4.	Selecciona todos los que correspondan a tu proyecto → clic derecho → Finalizar tarea.

2. Con línea de comandos (CMD o PowerShell)

Matar todos los procesos de Java:

```powershell
taskkill /F /IM java.exe /T
taskkill /F /IM javaw.exe /T
```

•	/F fuerza el cierre.
•	/IM indica el nombre de la imagen (ejecutable).
•	/T mata también los procesos hijos.

Ver primero cuáles están corriendo:

```powershell
tasklist | findstr java
```

3. Script rápido (batch)

Crea un archivo kill_java.bat con:

```batch
@echo off
echo Cerrando procesos de Java...
taskkill /F /IM java.exe /T
taskkill /F /IM javaw.exe /T
pause
```

Ejecutas ese .bat cuando quieras limpiar procesos colgados.

4. En PowerShell (más flexible)

Listar los procesos Java:

```powershell
Get-Process java, javaw
```

Matarlos todos:

```powershell
Get-Process java, javaw | Stop-Process -Force
```

### Notas

Con esto aseguras que no se queden instancias de JDK colgadas después de cerrar IntelliJ.

**Tags:** #workflow #killprocess #windows #java #intellij

---

## Convertir svg a jpg sin perder calidad

### Problema

Se busca convertir imágenes SVG a JPG sin perder calidad, para usarlas en presentaciones o documentos que no soportan SVG. Esto podría funcionar para cualquier otro formato de imagen.

### Solución

1. Con ImageMagick (la más flexible)

Si tu fuente es un SVG (vectorial), puedes exportarlo directo en 4K sin perder calidad:

```bash
magick -density 384 input.svg -resize 3840x2160 -quality 100 output.jpg
```

-	`-density 384` → aumenta la resolución de renderizado del vector.
-	`-resize 3840x2160` → fuerza resolución 4K (16:9).
-	`-quality 100` → máxima calidad de compresión JPG.

> Como el SVG es vectorial, puedes exportarlo incluso en 8K sin pérdida.

Si ya tienes una foto raster (JPG, PNG, etc.), entonces se usa interpolación:

```bash
magick input.jpg -resize 3840x2160 -quality 100 output_4k.jpg
```

2. Con Inkscape (para SVG → bitmap 4K o más)

```bash
# instalar Inkscape (si no lo tienes)
brew install --cask inkscape  # MacOS con Homebrew

# Exportar SVG a JPG en 4K
inkscape input.svg --export-type=jpg --export-filename=output.jpg --export-width=3840 --export-height=2160
```

3. Upscaling con IA (más calidad en fotos raster)

Si las imágenes son fotos y necesitas que de verdad ganen nitidez, puedes usar:

-	waifu2x-caffe (optimizado para fotos e ilustraciones).
-	Real-ESRGAN (más avanzado, soporta hasta 4K y 8K).

Ejemplo con Real-ESRGAN:

```bash
# Instalar Real-ESRGAN (requiere tener instalado Homebrew y git)
brew install real-esrgan

# Usar Real-ESRGAN para mejorar una foto a 4K
realesrgan-ncnn-vulkan -i input.jpg -o output_4k.jpg -s 4
```

En resumen:

-	SVG → JPG en 4K → usa magick -density + -resize.
-	Fotos raster → 4K con interpolación → magick -resize 3840x2160.
-	Fotos raster → 4K con mejora real → usar IA (Real-ESRGAN).

### Notas

Para fotos, la mejora con IA da mejores resultados que solo interpolar. Para gráficos vectoriales, exportar en alta resolución desde el origen es clave.

**Tags:** #workflow #performance #image-processing #svg #jpg #imagemagick #inkscape #ia

---