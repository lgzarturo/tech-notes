# Kubernetes

## Herramients para ver los pods en tiempo real

### Problema
Necesito monitorear el estado de los pods en mi clúster de Kubernetes en tiempo real.

### Solución

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

### Notas

**Recomendación**: k9s es una herramienta muy útil para la administración de clústeres de Kubernetes, ya que permite ver y gestionar recursos de manera interactiva. Puedes navegar entre diferentes recursos, ver logs, y realizar acciones como eliminar pods directamente desde la interfaz.

**Tags:** #kubernetes #kubectl #k9s #stern #monitoring

--- 
