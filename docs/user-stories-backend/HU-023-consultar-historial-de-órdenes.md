## HU-023: Consultar Historial de Órdenes

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero consultar el historial completo de órdenes para revisar pedidos anteriores, analizar ventas o recuperar información de órdenes específicas.

### Criterios de Aceptación

**Acceso al Historial:**
- Desde la página de órdenes, el filtro de fecha permite seleccionar periodos anteriores
- Por defecto, la vista muestra "Hoy"
- Owner puede cambiar a "Ayer", "Últimos 7 días", "Este mes", o rango personalizado

**Filtro de Fecha Personalizado:**
- Al seleccionar "Personalizado", abrir date picker de rango
- Permite seleccionar fecha inicial y fecha final

**Órdenes Históricas:**
- Incluir órdenes en todos los estados (Pendiente, Preparación, Lista, Cerrada)
- Ordenar por fecha/hora de creación (más reciente primero)

**Información Visible:**
- Las mismas columnas que la vista principal
- Todas las órdenes históricas muestran su estado final
- Click en una orden abre su detalle completo

**Búsqueda en Historial:**
- El campo de búsqueda funciona también en historial
- Permite buscar por número de orden en cualquier fecha
- Buscar orden específica sin importar el rango de fecha activo

**Exportación de Historial (Opcional):**
- El CSV incluye: número orden, fecha, hora, estado, items, total, notas
- El nombre del archivo incluye el rango de fechas (ej: "ordenes_2026-01-20_2026-01-26.csv")

**Paginación en Historial:**
- Si hay muchas órdenes, implementar paginación
- Información de paginación: "Mostrando 1-25 de 200 órdenes"

**Estados de Carga:**

**Manejo de Errores:**

**Estadísticas Rápidas del Periodo:**
  - Total de órdenes
  - Total de ventas
  - Ticket promedio
- Este resumen aparece en la parte superior de la lista

**Permisos:**
- Solo Owner puede acceder a historial completo
- Cajero solo puede ver órdenes del día actual

### Escenarios

9. **Rango inválido**: Owner selecciona fecha final antes de fecha inicial, ve error "Rango de fechas inválido", no se ejecuta la búsqueda
10. **Paginación en historial grande**: Owner selecciona "Este mes" con 500 órdenes, ve primeras 25 con paginación, navega a página 5 para ver órdenes 101-125

---

## Resumen de Estados de Órdenes

**Estados Disponibles:**

**Flujo de Estados:**
```
Pendiente → Preparación → Lista → Cerrada
```

**Restricciones:**
- No se puede saltar estados
- No se puede retroceder estados
- Cerrada es estado final (no cambia)

---

## Navegación en Módulo de Órdenes

**URLs:**
- `/orders` → Lista de órdenes
- `/orders/[id]` → Detalle de orden específica

**Breadcrumbs:**
- `/orders`: Dashboard > Órdenes
- `/orders/[id]`: Dashboard > Órdenes > Orden #XXX

**Acciones desde Órdenes:**

---

## Notas Técnicas

**Actualización en Tiempo Real:**
- Implementar WebSocket o polling (cada 10-15 segundos)
- Actualizar lista cuando hay cambios en órdenes
- Notificar cambios si usuario tiene detalle abierto
- Optimizar para no hacer requests innecesarios

**Numeración de Órdenes:**
- Generar número secuencial automático
- Formato: #001, #002, #003...
- Considerar reinicio diario o secuencia continua
- Asegurar unicidad con índice en base de datos

**Cálculo de Totales:**
- Subtotal: Suma de (precio × cantidad) de todos los productos
- Impuesto: Subtotal × (% impuesto configurado)
- Total: Subtotal + Impuesto
- Almacenar totales calculados en la orden (no recalcular cada vez)

**Performance:**
- Índices en: estado, fecha_creacion, numero_orden
- Paginación para listas grandes
- Caché de órdenes activas (Pendiente, Preparación, Lista)
- Lazy loading de órdenes históricas

**Timestamps:**
- created_at: Fecha/hora de creación
- updated_at: Última actualización
- Timestamp por cada cambio de estado (opcional)
- Zona horaria del restaurante

**Soft Delete:**
- No implementar eliminación de órdenes
- Todas las órdenes se mantienen en el sistema
- Estado "Cerrada" es el estado final

**Permisos:**
- Owner: Acceso completo (crear, ver, editar, historial)
- Cajero: Crear, ver y cambiar estados (solo órdenes del día)
- Validar permisos en frontend y backend

**Canal:**
- Para MVP: Solo "Mostrador" (fijo)
- Preparar estructura para futuros canales (Delivery, Para llevar, etc.)
