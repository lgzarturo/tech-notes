# Checklist de Documentación de Código Python

Este checklist se basa en estándares como PEP 257 (Docstring Conventions) y PEP 8 (Style Guide for Python Code).

## 1. **Docstrings (PEP 257)**

- [ ] **Módulos:**
  - [ ] ¿Tiene un docstring al inicio del archivo?
  - [ ] ¿Describe el propósito general del módulo?
  - [ ] ¿Incluye una breve descripción de su contenido principal (clases, funciones importantes)?
  - [ ] ¿Menciona autores, fecha o versión si es relevante?
- [ ] **Clases:**
  - [ ] ¿Tiene un docstring inmediatamente después de la definición de la clase?
  - [ ] ¿Describe el propósito de la clase y su responsabilidad principal?
  - [ ] ¿Explica los atributos importantes de la clase (instancia y clase)?
  - [ ] ¿Menciona cualquier relación con otras clases (herencia, composición)?
- [ ] **Métodos y Funciones:**
  - [ ] ¿Tiene un docstring inmediatamente después de la definición de la función/método?
  - [ ] ¿Describe qué hace la función/método (no cómo lo hace, a menos que sea complejo)?
  - [ ] ¿Explica cada parámetro (`Args:`): nombre, tipo, descripción y si es opcional/obligatorio?
  - [ ] ¿Describe el valor de retorno (`Returns:`): tipo y qué representa?
  - [ ] ¿Menciona las excepciones que puede levantar (`Raises:`)?
  - [ ] ¿Incluye ejemplos de uso (`Example:`) si la lógica es compleja o el uso no es obvio?
  - [ ] ¿Menciona cualquier efecto secundario (`Side Effects:`)?
  - [ ] ¿Describe precondiciones o postcondiciones si son críticas?
- [ ] **Formato de Docstrings:**
  - [ ] ¿Se utiliza un formato consistente (e.g., reStructuredText, Google, NumPy)? (Recomendado: reStructuredText para Sphinx).
  - [ ] ¿Los docstrings de una sola línea terminan en un punto y no tienen líneas en blanco?
  - [ ] ¿Los docstrings multilínea tienen una línea de resumen, una línea en blanco, y luego el cuerpo?
  - [ ] ¿Se usan comillas triples (`"""Docstring"""`)?

## 2. **Comentarios en Línea**

- [ ] **Claridad de Lógica Compleja:**
  - [ ] ¿Se utilizan comentarios para explicar secciones de código que no son inmediatamente obvias?
  - [ ] ¿Se evitan comentarios que solo repiten el código? (e.g., `x = x + 1 # Suma 1 a x`)
- [ ] **Decisiones de Diseño:**
  - [ ] ¿Se explican decisiones de diseño no estándar o compromisos (`trade-offs`)?
  - [ ] ¿Se justifican soluciones específicas para problemas complejos?
- [ ] **TODOs, FIXMEs, OPTIMIZEs:**
  - [ ] ¿Se utilizan marcadores estándar para tareas pendientes, errores conocidos o áreas de mejora?
  - [ ] ¿Son específicos y accionables?

## 3. **Nombres de Variables, Funciones y Clases (PEP 8)**

- [ ] **Claridad y Propósito:**
  - [ ] ¿Los nombres de variables son descriptivos y reflejan su contenido o propósito?
  - [ ] ¿Los nombres de funciones/métodos describen claramente la acción que realizan?
  - [ ] ¿Los nombres de clases son sustantivos que representan la entidad que modelan?
- [ ] **Consistencia:**
  - [ ] ¿Se sigue una convención de nomenclatura consistente (e.g., `snake_case` para funciones/variables, `CamelCase` para clases, `UPPER_CASE` para constantes)?
- [ ] **Evitar Abreviaciones Ambiguas:**
  - [ ] ¿Se evitan abreviaciones que puedan ser confusas o no estándar?

## 4. **Tipado (Type Hinting - PEP 484)**

- [ ] **Parámetros de Funciones/Métodos:**
  - [ ] ¿Todos los parámetros tienen anotaciones de tipo?
  - [ ] ¿Se utilizan tipos de la librería `typing` para estructuras complejas (e.g., `List`, `Dict`, `Optional`, `Union`)?
- [ ] **Valores de Retorno:**
  - [ ] ¿Todas las funciones/métodos tienen anotaciones de tipo para su valor de retorno?
- [ ] **Variables:**
  - [ ] ¿Se utilizan anotaciones de tipo para variables importantes o complejas, especialmente en asignaciones iniciales?
- [ ] **Consistencia:**
  - [ ] ¿Se aplica el tipado de forma consistente en todo el módulo/proyecto?

## 5. **Estructura y Organización del Código**

- [ ] **Cohesión y Acoplamiento:**
  - [ ] ¿Las clases y funciones tienen una única responsabilidad bien definida?
  - [ ] ¿Se minimiza el acoplamiento entre componentes?
- [ ] **Modularidad:**
  - [ ] ¿El código está dividido en módulos lógicos y manejables?
  - [ ] ¿Cada módulo tiene un propósito claro?
- [ ] **Consistencia de Estilo:**
  - [ ] ¿Se sigue un estilo de código consistente (e.g., PEP 8) en todo el proyecto? (Herramientas como `flake8`, `black`, `isort` pueden ayudar).

## 6. **Ejemplos y Pruebas (si aplica)**

- [ ] **Ejemplos en Docstrings:**
  - [ ] ¿Los ejemplos en los docstrings son correctos y fáciles de entender?
  - [ ] ¿Se pueden ejecutar directamente (doctests)?
- [ ] **Pruebas Unitarias:**
  - [ ] ¿Existen pruebas unitarias que demuestren el uso y el comportamiento esperado del código?
  - [ ] ¿Las pruebas sirven como una forma de documentación viva?

---

## Consideraciones Adicionales para Proyectos y Side Projects

- **README.md:**
  - [ ] ¿El `README.md` del proyecto describe claramente qué hace el proyecto, cómo instalarlo, cómo usarlo y cómo contribuir?
  - [ ] ¿Incluye ejemplos de uso?
- **Guía de Contribución:**
  - [ ] Si es un proyecto colaborativo, ¿existe una guía de contribución (`CONTRIBUTING.md`) que explique los estándares de código y documentación?
- **Generación Automática de Documentación:**
  - [ ] ¿Se utiliza Sphinx (con MyST para Markdown) para generar documentación a partir de los docstrings?
  - [ ] ¿La configuración de Sphinx está actualizada y genera la documentación correctamente?
