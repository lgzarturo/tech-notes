# 📘 Checklist de Ingeniería y Liderazgo Técnico

## 1. Hábitos diarios del ingeniero/líder técnico

- **Lee y escribe código todos los días**
  - Lectura: revisa proyectos OSS o código de tu equipo.
  - Escritura: commits pequeños y limpios.
- **Busca la simplicidad en cada solución**
  - Pregunta clave: _¿Se puede resolver de forma más clara y directa?_
- **Cuida la Developer Experience (DX)** hasta en tus scripts internos
  - Ejemplo: un script de despliegue con flags claros y mensajes de error comprensibles.
- **Revisa y reflexiona sobre errores**
  - Post-mortems técnicos y logs limpios → conviértelos en aprendizaje.

---

## 2. Principios de escritura de código

1. **Claridad primero**

   - El código debe ser leído 10x más de lo que se escribe.
   - Usa nombres completos y expresivos. Ejemplo: `average_session_duration` en lugar de `asd`.

2. **Convención antes que configuración**

   - Apóyate en convenciones estándar → reduce decisiones triviales.
   - Ejemplo: estructura homogénea en proyectos (carpetas, nombres).

3. **Experiencia del desarrollador (DX)**

   - Diseña APIs, endpoints o utilidades fáciles de entender.
   - La documentación debe estar lista “para el lunes siguiente”.

4. **Exigencia técnica y rigurosidad en PRs**

   - Commits atómicos con mensajes claros.
   - Code reviews como contratos de calidad, no como burocracia.

---

## 3. Guía de diseño de sistemas

- **Iterativo y modular**: divide en partes entendibles.
- **Monolito antes que microservicios**: empieza compacto, extrae lo necesario después.
- **Simplicidad elegante**: no compliques la arquitectura sin necesidad de negocio real.
- **Distribuido/global**: cuando escales a miles/millones, piensa en _colaboración descentralizada_.
  - Ejemplo: Git fue diseñado para que _cualquiera pudiese trabajar en Linux sin depender de un solo servidor_.

---

## 4. Trabajo en equipo y liderazgo técnico

### a) Rol del Tech Lead

- **Como mentor:**
  - Enseña fundamentos, explica el _por qué_ del diseño.
- **Como guía de visión:**
  - Define con claridad _cómo vamos a construir el sistema y por qué_.
- **Como facilitador:**
  - Escucha al equipo, fomenta que disfruten el proceso.
- **Como juez del código:**
  - Sé justo pero directo, protege la calidad del repo a toda costa.

### b) Ritual de equipo

- **Revisiones de código constructivas** → corregir y enseñar.
- **Post-mortems rápidos** después de un bug crítico → documentar, no culpar.
- **Stand-up meetings ligeras** → foco en obstáculos, no en enumerar tareas inútiles.
- **Demo semanal** de avances técnicos.

---

## 5. Buenas prácticas de largo plazo

- **Documentación viva**:
  - Un README claro, más un par de diagramas arquitectónicos simples.
- **Testing continuo**:
  - TDD si aplica, al menos cobertura de rutas críticas.
- **Automatización incremental**:
  - Scripts > procesos manuales recurrentes.
- **Escalable culturalmente**:
  - Normas de contribución → linters, guías de estilo, PR templates.

---

## 6. Checklist semanal

✅ **Código**

- [ ] Hice commits pequeños y significativos.
- [ ] Escribí código claro más que “listo para leet code challenge”.
- [ ] Implementé pruebas básicas en las rutas críticas.

✅ **Diseño**

- [ ] El sistema sigue simple y entendible.
- [ ] No agregué complejidad sin una necesidad concreta de negocio.

✅ **Equipo**

- [ ] Di feedback constructivo en revisiones.
- [ ] Documenté al menos 1 decisión de diseño.
- [ ] Escuché una sugerencia del equipo y la consideré.

✅ **Personal**

- [ ] Leí código ajeno y aprendí algo nuevo.
- [ ] Profundicé en fundamentos (CS, algoritmos, redes, bases de datos).
- [ ] Mejoré un script/herramienta para acelerar mi flujo.
