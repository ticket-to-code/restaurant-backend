## HU-031: Navegación y Persistencia en el POS

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero que el POS mantenga mi progreso si navego accidentalmente a otra página y que sea fácil volver a empezar una nueva venta.

### Criterios de Aceptación

**Persistencia del Carrito:**
- El contenido del carrito se guarda en localStorage/sessionStorage
- Si el usuario navega a otra página y vuelve, el carrito mantiene los productos
- La persistencia incluye:
  - Productos agregados
  - Cantidades
  - Notas

**Advertencia al Navegar:**
- Título: "¿Salir del punto de venta?"
- Mensaje: "Tienes una orden en progreso. Si sales, los productos se mantendrán para cuando vuelvas."
- Botones:
  - "Cancelar" (permanece en POS)
  - "Salir" (navega a la página solicitada)
- Esta advertencia NO aparece si el carrito está vacío

**Restauración al Volver:**
- Al volver a `/pos`, restaurar automáticamente:
  - Todos los productos con sus cantidades
  - Las notas ingresadas
  - Los totales calculados

**Limpiar Carrito:**
- También limpia la persistencia en localStorage

**Nueva Venta:**
- Después de completar un pago, el carrito se limpia automáticamente
- La persistencia se limpia
- El POS queda listo para nueva orden

**Timeout de Persistencia (Opcional):**
- Si el carrito persiste por más de 24 horas sin actividad, limpiarlo automáticamente

**Botón Nueva Venta:**

**Acceso Directo desde Otras Páginas:**
- Si hay carrito persistido, restaurarlo automáticamente

### Escenarios

---
