---
title: Hostinger
tags: [devops, hosting, tools]
category: devops
status: draft
created: 2025-10-31
updated: 2025-10-31
related: []
---

## Hostinger

Hostinger es un proveedor de servicios de alojamiento web que ofrece una variedad de planes de hosting, incluyendo alojamiento compartido, VPS y hosting en la nube. Es conocido por su interfaz fácil de usar, precios competitivos y buen rendimiento.

---

## ¿Como activar la geolocalización IP en Hostinger?

### Activar la geolocalización IP en Hostinger

**Problema:**

Es necesario activar la geolocalización IP en un sitio web alojado en Hostinger para personalizar el contenido según la ubicación del usuario.

**Solución:**

Para activarlo y utilizarlo con `.htaccess`, sigue estos pasos:

1. **Activar GeoIP en .htaccess**:

    Para habilitar GeoIP, debes agregar la siguiente línea a tu archivo `.htaccess`:

    ```bash
    GeoIPEnable On
    ```

    Esto activa la funcionalidad GeoIP en tu sitio web.

2. **Editar el archivo .htaccess**:

    Para editar el archivo `.htaccess`, puedes hacerlo a través del panel de control de tu hosting. Aquí te explico cómo hacerlo en hPanel y cPanel:

    - **hPanel**: Accede a **Archivos** → **Administrador de archivos**, selecciona tu dominio y ve a la carpeta **public_html**. Haz clic derecho en el archivo `.htaccess` y selecciona **Editar**.
    - **cPanel**: Ve a **Administrador de archivos** → **public_html**. Si no ves el archivo `.htaccess`, asegúrate de que la opción para mostrar archivos ocultos esté activada.

3. **Agregar reglas de acceso por país**:

    Una vez que GeoIP esté habilitado, puedes bloquear o permitir el acceso a tu sitio desde ciertos países. Por ejemplo, para bloquear el acceso a los archivos `wp-login.php` y `xmlrpc.php` desde cualquier país excepto el Reino Unido, Estados Unidos e India, agrega el siguiente código a tu archivo `.htaccess`:

    ```bash
    RewriteEngine on
    RewriteCond %{ENV:GEOIP_COUNTRY_CODE} !^(GB|US|IN)$
    RewriteRule (wp-login|xmlrpc).php$ - [F,L]
    ```

    Este código reescribe las reglas para que cualquier acceso a esos archivos desde fuera de los países especificados sea denegado.

4. **Verificar la configuración**

    Después de agregar las reglas, verifica que funcionen correctamente. Puedes crear un archivo PHP Info para asegurarte de que GeoIP esté funcionando.

    Con estos pasos, habrás activado GeoIP en tu sitio web de Hostinger utilizando `.htaccess`.

**Notas:**

- Asegúrate de tener acceso al archivo `.htaccess` y de que tu plan de hosting soporte la funcionalidad GeoIP.
- Siempre realiza una copia de seguridad del archivo `.htaccess` antes de hacer cambios, ya que errores en este archivo pueden causar problemas en el sitio web.
- Puedes personalizar las reglas según tus necesidades específicas de geolocalización.

**Tags:** #devops #hosting #tools

---
