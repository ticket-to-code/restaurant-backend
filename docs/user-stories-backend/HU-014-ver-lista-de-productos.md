## HU-014: Ver Lista de Productos

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero ver todos los productos del menú organizados por categoría para tener control completo sobre los items que ofrezco y poder gestionarlos fácilmente.

### Criterios de Aceptación

**Filtro por Categoría:**
- Dropdown con opciones:
  - "Todas las categorías" (opción por defecto)
  - Lista de todas las categorías existentes
- Al seleccionar una categoría, la tabla muestra solo productos de esa categoría

**Tabla de Productos:**
- Columnas visibles:
  - Imagen (thumbnail pequeño, 60x60px)
  - Nombre (texto, ordenable)
  - Categoría (badge con nombre de categoría)
  - Precio (formato moneda, ordenable)
  - Estado (badge: Disponible/No disponible)
  - Acciones (botones de editar y toggle estado)
- Las filas se pueden ordenar por nombre (A-Z o Z-A) o por precio (menor a mayor, mayor a menor)
- Cada fila muestra toda la información del producto de forma clara

**Imagen del Producto:**

**Badge de Categoría:**
- Si el filtro está activo en una categoría, los badges de esa categoría se destacan visualmente

**Formato de Precio:**
- Usar símbolo de moneda configurado en el sistema (ej: "$", "€", "S/")
- Formato con separador de miles y 2 decimales (ej: "$1,250.00")

**Estados del Producto:**
- Disponible (badge verde): El producto está activo y disponible para venta en el POS
- No disponible (badge gris): El producto existe pero no está disponible para venta

**Acciones Rápidas:**
- Toggle switch para cambiar estado Disponible/No disponible

**Ordenamiento por Defecto:**
- Los productos se muestran ordenados alfabéticamente (A-Z) por nombre
- Al cargar la página, el encabezado "Nombre" muestra indicador de orden ascendente

**Paginación:**
- Si hay más de 20 productos, implementar paginación
- Botones: Anterior, 1, 2, 3, Siguiente

**Búsqueda Rápida:**
- Búsqueda en tiempo real mientras se escribe (debounce de 300ms)
- Busca en nombre y categoría del producto

**Estados de Carga:**

**Manejo de Errores:**

**Permisos:**
- Esta página solo es accesible para usuarios con rol Owner
- Si un Cajero intenta acceder, ver página 403

### Escenarios

1. **Ver lista con productos existentes**: Owner accede a `/menu/productos`, ve tabla con 15 productos mostrando imagen, nombre, categoría, precio, estado y botones de acción
19. **Cajero intenta acceder**: Usuario Cajero intenta navegar a `/menu/productos`, ve página 403 "No tienes permisos para acceder a esta sección"

---
