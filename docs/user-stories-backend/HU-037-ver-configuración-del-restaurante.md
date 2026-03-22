## HU-037: Ver Configuración del Restaurante

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero ver la configuración actual de mi restaurante para conocer los datos registrados y verificar que la información esté correcta.

### Criterios de Aceptación

**Información Mostrada:**
- Los datos se muestran en formato de lectura (no editables directamente)
- Organización clara con labels y valores:
  - **Nombre del restaurante**: [Valor actual]
  - **Dirección**: [Valor actual]
  - **Moneda**: [Símbolo y código, ej: "$ - USD (Dólar estadounidense)"]
  - **Impuesto**: [Porcentaje, ej: "18%"]

**Botón Editar:**
- Los campos se convierten en inputs editables

**Estado Inicial (Primera Configuración):**
- Si el restaurante no tiene configuración guardada (registro nuevo):

**Valores por Defecto (Primera Configuración):**
- Nombre: Vacío (debe completarse)
- Dirección: Vacío (opcional)
- Moneda: "USD - Dólar estadounidense" (predeterminado)
- Impuesto: "0%" (predeterminado)

**Estados de Carga:**
- La carga debe completarse en menos de 2 segundos

**Manejo de Errores:**

**Permisos:**
- Esta página solo es accesible para usuarios con rol Owner
- Si un Cajero intenta acceder, ver página 403 "No tienes permisos para acceder a esta sección"

### Escenarios

1. **Ver configuración existente**: Owner accede a `/settings`, ve configuración actual: "Restaurante El Sabor", "Calle Principal 123", "$ - USD", "18%"
9. **Cajero intenta acceder**: Usuario Cajero intenta navegar a `/settings`, ve página 403 "No tienes permisos para acceder a esta sección"

---
