---
title: Kubernetes
tags: [devops, kubernetes, containers, tools]
category: devops
status: draft
created: 2025-10-05
updated: 2025-10-05
related: []
---

## Kubernetes

---

### Herramientas para ver los pods en tiempo real

**Problema:**

Necesito monitorear el estado de los pods en mi clúster de Kubernetes en tiempo real.

**Solución:**

- **Opción 1**: Usar el comando nativo de kubectl con la opción --watch para observar los cambios en los pods.

```bash
kubectl get pods -n <namespace> --watch
```

- **Opción 2**: Usar la herramienta k9s, que proporciona una interfaz de usuario en la terminal para interactuar con el clúster de Kubernetes.

```bash
# Asegúrate de tener k9s instalado previamente
k9s -n <namespace>
```

> Para instalar k9s, puedes seguir las instrucciones en su [repositorio oficial](https://github.com/derailed/k9s/releases).

- **Opción 3**: Kubectl top, para ver el uso de recursos en tiempo real.

```bash
kubectl top pods -n <namespace> --watch
```

> Requiere tener el Metrics Server instalado en el clúster.

- **Opción 4**: Usar Stern, para revisar los logs de varios pods al mismo tiempo.

```bash
stern <pod-name> -n <namespace>
```

**Notas:**

- Reemplaza `<namespace>` con el namespace que deseas monitorear. Si no especificas un namespace, se usará el namespace por defecto.
- Puedes filtrar los pods por nombre usando etiquetas o patrones en k9s y Stern.

**Recomendación:**

k9s es una herramienta muy útil para la administración de clústeres de Kubernetes, ya que permite ver y gestionar recursos de manera interactiva. Puedes navegar entre diferentes recursos, ver logs, y realizar acciones como eliminar pods directamente desde la interfaz.

**Tags:** #kubernetes #kubectl #k9s #stern #monitoring

---

### Reiniciar un pod en Kubernetes

**Problema:**

Cuando un pod en Kubernetes está en un estado no deseado (por ejemplo, CrashLoopBackOff), necesito reiniciarlo para que vuelva a funcionar correctamente.

**Solución:**

**Opción 1**: Eliminar el pod manualmente. Kubernetes automáticamente recreará el pod si está gestionado por un Deployment, ReplicaSet, o StatefulSet.

```bash
kubectl delete pod <pod-name> -n <namespace>
```

> Kubernetes recreará el pod automáticamente si está gestionado por un controlador.

**Opción 2**: Si quieres reiniciar todos los pods en un Deployment específico, puedes usar el siguiente comando para forzar un reinicio:

```bash
kubectl rollout restart deployment <nombre-del-deployment> -n <namespace>
```

**Notas:**

Nunca intentes reiniciar un pod directamente con `kubectl exec` o similares, eso no es una práctica recomendada en Kubernetes. Siempre es mejor dejar que el controlador gestione la recreación de los pods.

**Tags:** #kubernetes #pods #reinicio

---

### Obtener logs de un pod en Kubernetes con stern

**Problema:**

La herramienta `kubectl logs` solo permite ver los logs de un pod a la vez, lo que puede ser ineficiente cuando se trabaja con múltiples pods.

**Solución:**

Usar la herramienta `stern`, que permite ver los logs de múltiples pods en tiempo real y filtrar por nombre de pod o etiquetas.

```bash
stern <nombre-del-pod> -n <namespace>
```

Si no quieres que te muestre nada del historial y solo los logs nuevos, puedes usar la opción `--since`:

```bash
stern <nombre-del-pod> -n <namespace> --since 1m
```

o también puedes usar `--tail` para limitar la cantidad de líneas que quieres ver:

```bash
stern <nombre-del-pod> -n <namespace> --tail 100
```

**Notas:**

Este comando:

- Filtra los pods por el nombre proporcionado.
- Muestra los logs en tiempo real.
- No muestra logs históricos si se usa `--since` o `--tail`.

**Tags:** #kubernetes #stern #logs

---
