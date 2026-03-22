## HU-010: Ver Lista de Categorías

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero ver todas las categorías del menú del restaurante para tener una visión organizada de cómo está estructurado mi menú y poder gestionar las categorías fácilmente.

### Criterios de Aceptación

**Tabla de Categorías:**
- Columnas visibles:
  - Nombre (texto, ordenable)
  - Productos (número de productos en la categoría)
  - Estado (badge: Activa/Inactiva)
  - Acciones (botones de editar y toggle estado)
- Cada fila muestra:
  - Número de productos asociados (ej: "12 productos")
  - Badge de estado: "Activa" (verde) o "Inactiva" (gris)
  - Toggle switch para activar/desactivar

**Ordenamiento por Defecto:**
- Las categorías se muestran ordenadas alfabéticamente (A-Z) por defecto
- Al cargar la página, el encabezado "Nombre" muestra un indicador de orden ascendente

**Acciones Rápidas:**

**Estados de Categoría:**
- Activa: La categoría y sus productos están disponibles para selección en el POS
- Inactiva: La categoría y sus productos NO están disponibles en el POS pero se mantienen en el sistema

**Conteo de Productos:**
- El conteo incluye todos los productos (disponibles y no disponibles)

**Estados de Carga:**
- La carga inicial debe completarse en menos de 2 segundos

**Manejo de Errores:**
- El toggle vuelve a su estado anterior si falla la actualización

**Permisos:**
- Esta página solo es accesible para usuarios con rol Owner
- Si un Cajero intenta acceder, ver página 403

### Escenarios

1. **Ver lista con categorías existentes**: Owner accede a `/menu/categorias`, ve tabla con 5 categorías ordenadas alfabéticamente con sus nombres, conteo de productos, estados y botones de acción
14. **Cajero intenta acceder**: Usuario con rol Cajero intenta navegar a `/menu/categorias`, ve página 403 con mensaje "No tienes permisos para acceder a esta sección"

---
