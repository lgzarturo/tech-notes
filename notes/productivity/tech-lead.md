---
title: Tech Lead Notes
tags: [leadership, management, productivity]
category: productivity
status: draft
created: 2023-10-01
updated: 2023-10-01
---

## Tech Lead Notes

Estas son algunas ideas y notas sobre el rol de un Tech Lead:

- **Comunicación efectiva**: Es crucial mantener una comunicación clara y abierta con el equipo y otras partes interesadas.
- **Mentoría**: Un Tech Lead debe guiar y apoyar a los desarrolladores menos experimentados, ayudándoles a crecer en sus habilidades.
- **Toma de decisiones**: Debe ser capaz de tomar decisiones técnicas informadas y defenderlas ante el equipo y la dirección.
- **Gestión del tiempo**: Priorizar tareas y gestionar el tiempo de manera efectiva es esencial para cumplir con los plazos del proyecto.
- **Colaboración**: Fomentar un ambiente de colaboración y trabajo en equipo es clave para el éxito del proyecto.

---

### Reglas de los tickets

**Problema:**

A veces los tickets no están bien definidos o son demasiado amplios.

**Solución:**

Las reglas que uso para gestionar tickets, son estas:

**Incidencias críticas:**

- Si "Impacto = Bloquea ventas" → cambiar Status automáticamente a Priorizado + notificación Slack/Teams al canal de soporte.
- 70% (estratégico del manager) – 30% (soporte/incidencias): Si aparecen más incidencias críticas → negocias con tu manager qué parte del 70% se debe posponer.

**Proyectos atorados:**

- Si una tarea está 5 días en In Progress sin avance → notificar al Líder de IT.
- Vistas por prioridad y por responsable.
- Reportes semanales: tiempo invertido en proyectos vs incidencias.

**QA automático:**

- Cuando un bug cambia a En Progreso Finalizado → asignar automáticamente al proceso para validación.

#### Beneficios directos

- Nada se pierde → todo bug tiene flujo definido y plantilla clara.
- Lo estratégico tiene espacio reservado → no se ahoga en tickets.
- Cesar ve avances reales y entiende cómo las incidencias afectan al plan.
- Refuerzas liderazgo → comunicas con métricas y no con percepciones.
- Separas lo estratégico de lo reactivo.
- Tienes reportes y dashboards para reforzar tu liderazgo.

#### Dashboard de Liderazgo

Crea un Dashboard llamado "Visión General IT" con estos widgets:

- Gráfico de horas (pie chart): % de tiempo estratégico vs soporte en la semana.
- Lista dinámica: Solo "Proyectos Estratégicos" con % completado.
- Gráfico de barras: Bugs críticos abiertos vs cerrados en los últimos 30 días.
- Burnup Chart (avance): Mostrar progreso de Proyectos BE 2025.
- Gráfico Donut → % tiempo en Proyectos vs Incidencias.
- Lista dinámica filtrada → Solo Proyectos Estratégicos con % completado.
- Barras comparativas → Bugs críticos abiertos vs cerrados (últimos 30 días).
- Line Chart (Burnup) → Avance acumulado de Proyectos BE 2025.

👉 Este dashboard es tu "control de cabina" y también el reporte visual para tu manager ✅.

#### Listado maestro de proyectos y seguimiento

Lo que veo en tu captura es que las fechas están incompletas; eso puede causar que pierdas visibilidad.

✅ Recomendaciones prácticas:

- Cada iniciativa estratégica debe tener fecha inicio + fecha fin + entregables claros.
- Ten una vista Gantt/Calendario solo para proyectos (no incidencias).
- Haz revisiones semanales con tu manager mostrando:
- Avance % de proyectos principales.
- Principales incidencias críticas resueltas o en progreso.
- Riesgos (dependencias bloqueadas, falta de recursos).

#### Refuerzo de liderazgo en la práctica

Tu rol no es solo ejecutar, sino traducir las interrupciones a un lenguaje de negocio. Ejemplo para tu manager:

> "Esta semana atendimos un bug P1 en pagos que bloqueaba ventas, tomó 20h de soporte. Esto desplazó 1 semana el avance del ‘Plan de Lealtad’. Propongo ajustar la planificación."

**👉 Con esto:**

- Muestras control sobre lo que pasa.
- Demuestras que entiendes la prioridad del negocio.
- Refuerzas tu liderazgo convirtiendo datos en decisiones.

**✅ Resumido:**

- Separa proyectos estratégicos, incidencias y mantenimiento en listas diferentes.
- Documenta incidencias con una plantilla clara.
- Usa un sistema de prioridad consensuado (P1–P4).
- Reserva capacidad para lo imprevisto y negocia con datos.
- Mantén un listado maestro de proyectos con fechas y reportes.
- Refuerza tu liderazgo comunicando impacto de soporte en el roadmap estratégico.

#### Definir Custom Fields (Campos personalizados)

Esto es clave porque te permite tomar decisiones rápidas.
Agrega a todas las listas un conjunto estándar de campos:

**Impacto Negocio (dropdown):**

- ⚠️ Bloquea ventas
- 🔴 Alto impacto
- 🟠 Medio impacto
- 🟢 Bajo impacto

**Prioridad (flag):**

- P1 – Crítico
- P2 – Alta
- P3 – Media
- P4 – Baja

**Tipo de Tarea (dropdown):**

- Proyecto Estratégico
- Bug / Incidencia
- Mejora / Deuda técnica

Estimación Horas (number) → ya lo usas, mantenlo.

👉 Con estos campos, puedes filtrar y crear dashboards en segundos.

#### Documentar incidencias

Configura una Tarea Plantilla llamada: "Reporte de Incidencia / Bug" con estos elementos:

- Título estandarizado: Bug <Módulo> – <Problema>
- Custom Fields prellenados (Tipo = Bug, Prioridad vacía para que soporte seleccione).
- Checklist dentro de la descripción:
  ⬜ Steps para replicar
  ⬜ Impacto en usuarios/ventas
  ⬜ Evidencia (screenshots / videos adjuntos)
  ⬜ Workaround si existe
  
👉 Así soporte puede levantar tareas consistentes y tú solo evaluar prioridad.

#### Flujos de trabajo (Statuses) diferenciados

Puedes personalizar "Statuses" por lista.

Ejemplo para Proyectos Estratégicos:

- 📋 To Do → 🚧 In Progress → ✅ Done

Ejemplo para Soporte e Incidencias:

- 🟡 Reportado → 🔍 En análisis → 📌 Priorizado → 🚧 En progreso → 🧪 En pruebas QA → ✅ Cerrado

👉 Esto refleja la realidad distinta de cada tipo de trabajo.

**Notas:**

- Revisa y ajusta estas reglas cada 2 semanas al inicio.
- Comunica estos cambios al equipo y stakeholders.
- Usa datos y dashboards para reforzar tu liderazgo.
- Mantén un enfoque proactivo en la identificación de riesgos.
- Documenta lecciones aprendidas y mejores prácticas.
- Comparte conocimientos y recursos con el equipo.
- Fomenta una cultura de retroalimentación y mejora continua.
- Celebra los logros y reconoce el esfuerzo del equipo.
- Promueve la colaboración y el trabajo en equipo.
- Fomenta la diversidad y la inclusión en el equipo.
- Mantente actualizado con las tendencias y mejores prácticas en tecnología y liderazgo.

**Tags:** #tech-lead #liderazgo #gestión #productividad #soporte #proyectos #dashboard #reportes #comunicación #mentoría #toma-decisiones #colaboración #mejora-continua

---
