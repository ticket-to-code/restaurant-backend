## HU-009: Navegación y Acceso al Dashboard

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario autenticado (Owner o Cajero), quiero acceder fácilmente al dashboard desde cualquier parte de la aplicación para tener siempre disponible la visión general del estado del restaurante.

### Criterios de Aceptación

**Acceso Directo al Dashboard:**
- El dashboard es la página de aterrizaje después de login exitoso
- La URL del dashboard es `/dashboard`
- El dashboard está disponible tanto para Owner como para Cajero

**Breadcrumb:**
- El dashboard NO muestra breadcrumb ya que es la página principal
- Otras páginas sí muestran breadcrumb con "Dashboard" como primer nivel clickeable

**Redirección por Defecto:**

### Escenarios

1. **Login exitoso redirige a dashboard**: Usuario ingresa credenciales correctas, hace clic en "Iniciar Sesión", es redirigido automáticamente a `/dashboard`
8. **Página 404 con botón al dashboard**: Usuario autenticado intenta acceder a `/pagina-inexistente`, ve página 404 con mensaje y botón "Ir al Dashboard", hace clic y es redirigido a `/dashboard`

---

## Resumen de Componentes del Dashboard

### Para Owner:
- ✅ Card: Ventas del día
- ✅ Card: Órdenes abiertas (clickeable → `/orders`)
- ✅ Card: Ticket promedio
- ✅ Card: Productos más vendidos (top 5)
- ✅ Manejo de errores por card

### Para Cajero:
- ✅ Card: Órdenes abiertas (clickeable → `/orders`)
- ✅ Sección: Lista de órdenes pendientes (últimas 10)
- ✅ Actualización automática cada 30 segundos
- ✅ Manejo de errores

### Cálculos Backend:
- ✅ Total ventas del día (desde 00:00 a 23:59)
- ✅ Conteo órdenes abiertas por estado
- ✅ Ticket promedio (ventas ÷ órdenes cerradas)
- ✅ Top 5 productos más vendidos del día
- ✅ Caché con TTL 30s e invalidación al actualizar orden
- ✅ Polling frontend cada 30s

### Navegación:
- ✅ Dashboard como landing page post-login
- ✅ Acceso desde menú lateral (siempre visible)
- ✅ Acceso desde logo/nombre app en header
- ✅ Estado activo en menú cuando está en dashboard

---

## Notas Técnicas

**Actualización en Tiempo Real:**
- Implementar WebSocket para notificaciones de cambios en órdenes (ideal)
- Alternativa: Polling cada 30 segundos (más simple para MVP)
- Invalidación de caché al crear/actualizar/cerrar órdenes

**Performance:**
- Cálculos de KPIs en backend con SQL optimizado
- Usar índices en campos de fecha y estado de órdenes
- Caché de 30s para reducir carga en DB
- Paginación en lista de órdenes pendientes (aunque MVP muestra solo 10)

**Formato de Moneda:**
- Usar la moneda configurada en `/settings` del restaurante
- Formato con separador de miles y 2 decimales
- Símbolo de moneda según configuración (ej: "$", "€", "S/")

**Zona Horaria:**
- Usar la zona horaria configurada en `/settings`
- Todos los cálculos de "día actual" respetan esta zona horaria
