---
title: Dns Records
tags: [tools, dns, networking, records]
category: tools
status: draft
created: 2025-12-16
updated: 2025-12-16
related: []
---

## Dns Records

Los registros DNS (Domain Name System) son entradas en una base de datos que traducen nombres de dominio legibles por humanos (como www.arthurolg.com) en direcciones IP numéricas.

Existen varias herramientas confiables que puede utilizar para validar los registros DNS configurados para su dominio. Estas herramientas permiten verificar que los registros **CNAME** y **TXT** se hayan propagado correctamente y estén configurados según las instrucciones.

---

### **1. Herramientas en Línea**

Estas herramientas son fáciles de usar y no requieren instalación:

#### **a. MXToolbox**

- **URL:** [https://mxtoolbox.com/](https://mxtoolbox.com/)
- **Uso:**
  - Ingresa el nombre del registro (por ejemplo, `mte1._domainkey.arthurolg.com`) en la sección de búsqueda.
  - Selecciona el tipo de registro que deseas verificar (CNAME o TXT).
  - Revisa los resultados para confirmar que los valores coincidan con los proporcionados.

#### **b. DNS Checker**

- **URL:** [https://dnschecker.org/](https://dnschecker.org/)
- **Uso:**
  - Ingresa el nombre del registro (por ejemplo, `mte1._domainkey.arthurolg.com` o el dominio raíz para el registro TXT).
  - Selecciona el tipo de registro (CNAME o TXT).
  - Verifica la propagación global de los registros.

#### **c. Google Admin Toolbox**

- **URL:** [https://toolbox.googleapps.com/apps/dig/](https://toolbox.googleapps.com/apps/dig/)
- **Uso:**
  - Ingresa el nombre del registro.
  - Selecciona el tipo de consulta (CNAME o TXT).
  - Haz clic en "Dig" para obtener los resultados.

---

### **2. Herramientas de Línea de Comandos**

Si tienes acceso a una terminal, puedes usar comandos para verificar los registros DNS:

#### **a. Comando `nslookup`**

- **Uso:**

  - Abre una terminal.
  - Ejecuta el comando:

    ```bash
    nslookup -type=CNAME mte1._domainkey.arthurolg.com
    ```

    Para registros TXT:

    ```bash
    nslookup -type=TXT arthurolg.com
    ```

#### **b. Comando `dig`**

- **Uso:**

  - Ejecuta el comando:

    ```bash
    dig CNAME mte1._domainkey.arthurolg.com
    ```

    Para registros TXT:

    ```bash
    dig TXT arthurolg.com
    ```

#### **c. Comando `host`**

- **Uso:**

  - Ejecuta el comando:

    ```bash
    host -t CNAME mte1._domainkey.arthurolg.com
    ```

    Para registros TXT:

    ```bash
    host -t TXT arthurolg.com
    ```

---

### **3. Herramientas de Proveedores de DNS**

Si tu proveedor de DNS ofrece herramientas de diagnóstico, puedes utilizarlas para verificar los registros directamente desde tu panel de control. Algunos proveedores como **Cloudflare**, **GoDaddy**, y **AWS Route 53** tienen opciones para comprobar la configuración de DNS.

---

### **Recomendación Final**

Para garantizar que los registros estén configurados correctamente:

1. Usa una combinación de herramientas en línea y de línea de comandos para validar los registros.
2. Espera al menos 15-30 minutos después de realizar cambios en los registros DNS, ya que la propagación puede tardar un poco.
3. Si encuentras problemas, revisa la configuración en tu proveedor de DNS y asegúrate de que los valores coincidan exactamente con los proporcionados.
