## HU-024: Interfaz Principal del POS

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero una interfaz de punto de venta clara y eficiente para tomar pedidos rápidamente y sin errores durante el servicio a clientes.

### Criterios de Aceptación

**Sección Izquierda: Catálogo de Productos**
- Filtros por categoría en tabs o pills horizontales:
  - "Todas" (muestra todos los productos)
  - Cada categoría activa del sistema
- Grid de productos con cards:
  - Nombre del producto
  - Precio
  - Badge "No disponible" si el producto no está disponible
- Cards clickeables para agregar al carrito
- Scroll vertical si hay muchos productos

**Sección Derecha: Carrito y Resumen**
- Lista de productos agregados mostrando:
  - Nombre del producto
  - Precio unitario
  - Controles de cantidad (-, cantidad, +)
  - Subtotal (precio × cantidad)
- Resumen de totales al final:
  - Subtotal
  - Impuesto (% y monto)
  - Total (destacado, grande)

**Filtro por Categoría:**
- La categoría activa se destaca visualmente
- "Todas" muestra todos los productos disponibles

**Búsqueda de Productos:**
- Búsqueda en tiempo real mientras se escribe (debounce de 300ms)
- Busca en nombre del producto
- Muestra solo productos que coincidan con la búsqueda

**Estado de Productos No Disponibles:**
- Productos marcados como "No disponible" se muestran con opacidad reducida
- Badge "No disponible" sobre la card
- No son clickeables (no se pueden agregar al carrito)

**Productos de Categorías Inactivas:**

**Estados de Carga:**
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**

**Permisos:**
- Tanto Owner como Cajero tienen acceso completo al POS

### Escenarios

---
