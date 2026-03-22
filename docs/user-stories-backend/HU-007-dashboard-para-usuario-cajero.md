## HU-007: Dashboard para Usuario Cajero

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario con rol Cajero, quiero ver un dashboard simplificado centrado en órdenes para enfocarme en las operaciones diarias sin distracciones de KPIs financieros.

### Criterios de Aceptación

**Card: Órdenes Abiertas**
- Título: "Órdenes abiertas"
- Valor principal: Número total de órdenes con estados "Pendiente", "Preparación" o "Lista"
- Desglose visual por estado:

**Sección: Órdenes Pendientes de Atención**
- Título: "Órdenes pendientes"
- Muestra lista de las últimas 10 órdenes con estados "Pendiente" o "Preparación" (excluye "Lista" y "Cerrada")
- Cada orden en la lista muestra:
  - Número de orden (ej: "#001")
  - Hora de creación (ej: "10:30 AM")
  - Total de la orden (ej: "$45.00")
- Las órdenes se ordenan por hora de creación (más reciente primero)

**Interacciones:**

**Estados de Carga:**
- La carga debe completarse en menos de 2 segundos

**Actualización en Tiempo Real:**
- El dashboard se actualiza automáticamente cada 30 segundos para reflejar nuevas órdenes
- Al crear una nueva orden desde el POS, el dashboard debe actualizarse automáticamente (WebSocket o polling)

**Manejo de Errores:**

**Elementos NO Visibles para Cajero:**
- Enfoque 100% operativo en órdenes

### Escenarios

---
