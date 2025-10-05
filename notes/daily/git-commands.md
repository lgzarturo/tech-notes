---
title: Git Commands
tags: [daily, git, commands, version-control]
category: daily
status: draft
created: 2025-10-05
updated: 2025-10-05
related: []
---

## Git Commands

100 Comandos útiles de Git, que te ayudarán a gestionar tus proyectos de manera eficiente y mantener un control de versiones adecuado.

Aquí hay algunos comandos básicos de Git que son útiles para el control de versiones:

1. `git init`: Inicializa un nuevo repositorio de Git.
2. `git clone <url>`: Clona un repositorio existente desde una URL.
3. `git add <archivo>`: Agrega un archivo al área de preparación (staging area).
4. `git commit -m "mensaje"`: Realiza un commit de los cambios en el área de preparación con un mensaje descriptivo.
5. `git status`: Muestra el estado actual del repositorio, incluyendo archivos modificados y no rastreados.
6. `git push`: Envía los cambios locales a un repositorio remoto.
7. `git pull`: Obtiene y fusiona cambios desde un repositorio remoto.
8. `git branch`: Muestra las ramas existentes en el repositorio.
9. `git checkout <rama>`: Cambia a una rama diferente.
10. `git merge <rama>`: Fusiona una rama en la rama actual.
11. `git log`: Muestra el historial de commits del repositorio.
12. `git diff`: Muestra las diferencias entre archivos o commits.
13. `git remote -v`: Muestra las URL de los repositorios remotos configurados.
14. `git stash`: Guarda temporalmente los cambios no confirmados para limpiar el área de trabajo.
15. `git stash pop`: Restaura los cambios guardados en el stash y los elimina del stash.
16. `git reset --hard <commit>`: Restablece el repositorio al estado de un commit específico, descartando todos los cambios posteriores.
17. `git fetch`: Descarga los cambios desde un repositorio remoto sin fusionarlos automáticamente.
18. `git rebase <rama>`: Aplica los cambios de la rama actual sobre otra rama, reescribiendo el historial de commits.
19. `git tag <nombre>`: Crea una etiqueta en un commit específico para marcar versiones importantes.
20. `git cherry-pick <commit>`: Aplica los cambios de un commit específico a la rama actual.
21. `git rm <archivo>`: Elimina un archivo del repositorio y del área de preparación.
22. `git mv <archivo_viejo> <archivo_nuevo>`: Renombra o mueve un archivo dentro del repositorio.
23. `git show <commit>`: Muestra los detalles de un commit específico, incluyendo los cambios realizados.
24. `git blame <archivo>`: Muestra quién hizo cada cambio en un archivo línea por línea.
25. `git config --global user.name "Tu Nombre"`: Configura el nombre de usuario para los commits.
26. `git config --global user.email "tu.email@example.com"`: Configura la dirección de correo electrónico para los commits.
27. `git clean -f`: Elimina archivos no rastreados del directorio de trabajo.
28. `git bisect`: Utiliza la búsqueda binaria para encontrar el commit que introdujo un error.
29. `git archive -o archivo.zip HEAD`: Crea un archivo ZIP del estado actual del repositorio.
30. `git reflog`: Muestra el historial de referencias, útil para recuperar commits perdidos.
31. `git submodule add <url> <ruta>`: Agrega un submódulo a tu repositorio.
32. `git submodule update --init --recursive`: Inicializa y actualiza los submódulos.
33. `git shortlog`: Muestra un resumen de los commits agrupados por autor.
34. `git gc`: Realiza una limpieza y optimización del repositorio.
35. `git remote add <nombre> <url>`: Agrega un nuevo repositorio remoto con un nombre específico.
36. `git remote remove <nombre>`: Elimina un repositorio remoto configurado.
37. `git log --oneline --graph --decorate --all`: Muestra un historial de commits compacto y visualmente estructurado.
38. `git diff <rama1> <rama2>`: Muestra las diferencias entre dos ramas específicas.
39. `git reset --soft <commit>`: Restablece el repositorio al estado de un commit específico, manteniendo los cambios en el área de preparación.
40. `git reset --mixed <commit>`: Restablece el repositorio al estado de un commit específico, manteniendo los cambios en el directorio de trabajo pero eliminándolos del área de preparación.
41. `git log --stat`: Muestra el historial de commits junto con un resumen de los cambios en cada archivo.
42. `git log -p`: Muestra el historial de commits junto con las diferencias detalladas de cada commit.
43. `git commit --amend`: Modifica el último commit, permitiendo cambiar el mensaje o agregar más cambios.
44. `git rebase -i <commit>`: Inicia una rebase interactiva para editar, reordenar o combinar commits.
45. `git stash list`: Muestra la lista de stashes guardados.
46. `git stash apply <stash>`: Aplica un stash específico sin eliminarlo de la lista de stashes.
47. `git tag -d <nombre>`: Elimina una etiqueta local.
48. `git push origin --tags`: Envía todas las etiquetas locales al repositorio remoto.
49. `git cherry`: Muestra los commits que están en la rama actual pero no en la rama especificada.
50. `git worktree add <ruta> <rama>`: Crea un nuevo árbol de trabajo para una rama específica en una ruta diferente.
51. `git worktree remove <ruta>`: Elimina un árbol de trabajo creado previamente.
52. `git instaweb`: Inicia un servidor web para navegar por el historial del repositorio.
53. `git notes add -m "nota"`: Agrega una nota a un commit específico.
54. `git notes show <commit>`: Muestra las notas asociadas a un commit específico.
55. `git blame -L <número_línea>,<número_línea> <archivo>`: Muestra quién hizo cambios en una línea específica de un archivo.
56. `git log --since="2 weeks ago"`: Muestra los commits realizados en las últimas dos semanas.
57. `git log --author="Nombre"`: Muestra los commits realizados por un autor específico.
58. `git log --grep="mensaje"`: Muestra los commits que contienen un mensaje específico.
59. `git diff --cached`: Muestra las diferencias entre el área de preparación y el último commit.
60. `git diff HEAD`: Muestra las diferencias entre el directorio de trabajo y el último commit.
61. `git diff <commit1> <commit2>`: Muestra las diferencias entre dos commits específicos.
62. `git reset HEAD <archivo>`: Elimina un archivo del área de preparación sin eliminar los cambios en el directorio de trabajo.
63. `git stash drop <stash>`: Elimina un stash específico de la lista de stashes.
64. `git stash clear`: Elimina todos los stashes guardados.
65. `git tag -a <nombre> -m "mensaje"`: Crea una etiqueta anotada con un mensaje descriptivo.
66. `git tag -l`: Muestra todas las etiquetas en el repositorio.
67. `git push origin <rama>`: Envía una rama específica al repositorio remoto.
68. `git pull --rebase`: Obtiene los cambios desde el repositorio remoto y los aplica sobre la rama actual usando rebase en lugar de merge.
69. `git fetch --all`: Descarga los cambios desde todos los repositorios remotos configurados.
70. `git rebase --continue`: Continúa un proceso de rebase que fue interrumpido por conflictos.
71. `git rebase --abort`: Cancela un proceso de rebase y restaura el estado anterior.
72. `git reflog expire --expire=now --all`: Limpia el reflog eliminando todas las entradas.
73. `git reflog delete <ref>`: Elimina una entrada específica del reflog.
74. `git submodule foreach 'git pull origin main'`: Actualiza todos los submódulos a la última versión de la rama principal.
75. `git submodule status`: Muestra el estado actual de los submódulos.
76. `git shortlog -s -n`: Muestra un resumen de los commits agrupados por autor, ordenados por número de commits.
77. `git gc --aggressive`: Realiza una limpieza y optimización más exhaustiva del repositorio.
78. `git remote set-url origin <nueva_url>`: Cambia la URL del repositorio remoto llamado "origin".
79. `git remote rename <viejo_nombre> <nuevo_nombre>`: Cambia el nombre de un repositorio remoto configurado.
80. `git log --follow <archivo>`: Muestra el historial de commits de un archivo específico, incluso si ha sido renombrado.
81. `git diff --name-only <commit1> <commit2>`: Muestra solo los nombres de los archivos que han cambiado entre dos commits específicos.
82. `git reset --merge <commit>`: Restablece el repositorio al estado de un commit específico, manteniendo los cambios en el directorio de trabajo y fusionando los cambios.
83. `git commit -a -m "mensaje"`: Realiza un commit de todos los archivos modificados y rastreados con un mensaje descriptivo.
84. `git commit --no-edit --amend`: Modifica el último commit sin cambiar el mensaje.
85. `git rebase -i HEAD~n`: Inicia una rebase interactiva para los últimos n commits.
86. `git stash branch <rama>`: Crea una nueva rama y aplica el stash más reciente en ella.
87. `git stash save "mensaje"`: Guarda los cambios no confirmados en un stash con un mensaje descriptivo.
88. `git tag -f <nombre> <commit>`: Fuerza la creación o actualización de una etiqueta en un commit específico.
89. `git push origin :<rama>`: Elimina una rama específica del repositorio remoto.
90. `git pull --ff-only`: Obtiene los cambios desde el repositorio remoto solo si se puede hacer un avance rápido (fast-forward).
91. `git fetch origin <rama>:<rama_local>`: Descarga una rama específica desde el repositorio remoto y la crea o actualiza en el repositorio local.
92. `git rebase --skip`: Omite el commit actual durante un proceso de rebase.
93. `git reflog show <ref>`: Muestra el historial de referencias para una referencia específica.
94. `git submodule sync`: Sincroniza las URLs de los submódulos con las configuraciones del repositorio principal.
95. `git shortlog -s -n --all`: Muestra un resumen de los commits agrupados por autor, incluyendo todas las ramas y etiquetas.
96. `git gc --prune=now`: Limpia el repositorio eliminando objetos no referenciados inmediatamente.
97. `git remote prune origin`: Elimina las referencias a ramas remotas que ya no existen en el repositorio remoto.
98. `git log --pretty=format:"%h - %an, %ar : %s"`: Muestra el historial de commits en un formato personalizado.
99. `git diff --stat <commit1> <commit2>`: Muestra un resumen estadístico de los cambios entre dos commits específicos.
100. `git reset --hard origin/<rama>`: Restablece la rama actual al estado de la rama remota, descartando todos los cambios locales.

---
