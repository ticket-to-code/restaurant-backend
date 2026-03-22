## HU-038: Editar Configuración del Restaurante

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero editar la configuración de mi restaurante para actualizar datos cuando sea necesario (cambio de dirección, ajuste de impuesto, etc.).

### Criterios de Aceptación

**Modo Edición:**
  - "Cancelar" (secundario, izquierda)
  - "Guardar cambios" (primario, derecha)

**Campo: Nombre del Restaurante**
- Label: "Nombre del restaurante *" (asterisco indica requerido)
- Input de texto
- Valor precargado con el nombre actual
- Mínimo 2 caracteres, máximo 100 caracteres
- Requerido

**Validaciones de Nombre:**

**Campo: Dirección**
- Label: "Dirección"
- Input de texto (o textarea de 2 líneas)
- Valor precargado con la dirección actual (o vacío si no hay)
- Máximo 200 caracteres
- Opcional

**Validaciones de Dirección:**
- Permitir dejarlo vacío

**Campo: Moneda**
- Label: "Moneda *" (requerido)
- Dropdown/Select con lista de monedas comunes
- Valor precargado con la moneda actual
- Opciones incluyen:
  - USD - Dólar estadounidense ($)
  - EUR - Euro (€)
  - PEN - Sol peruano (S/)
  - MXN - Peso mexicano ($)
  - COP - Peso colombiano ($)
  - CLP - Peso chileno ($)
  - ARS - Peso argentino ($)
  - (Agregar otras según necesidad)
- Requerido

**Campo: Impuesto**
- Label: "Impuesto (%) *" (requerido)
- Input numérico
- Valor precargado con el impuesto actual
- Acepta decimales (1 dígito, ej: 18.5)
- Rango: 0 a 100
- Requerido

**Validaciones de Impuesto:**
- Si es menor a 0, ajustar automáticamente a 0
- Permitir 0% (sin impuesto)
- Permitir decimales con 1 dígito (ej: 18.5, 16.7)

**Detección de Cambios:**

**Comportamiento del Botón Guardar:**

**Guardado Exitoso:**
- Si el guardado es exitoso:
  - Volver a modo lectura automáticamente
  - Los cambios se aplican inmediatamente en todo el sistema

**Aplicación de Cambios:**
- Cambio de nombre: Se refleja en header, facturas, tickets
- Cambio de dirección: Se refleja en tickets (si se usa)
- Cambio de moneda: Se aplica a todos los precios, totales, reportes
- Cambio de impuesto: Se aplica a todas las nuevas ventas (no afecta ventas anteriores)

**Manejo de Errores:**
- El formulario permanece en modo edición con los datos ingresados

**Botón Cancelar:**
- Volver a modo lectura mostrando los valores originales

**Modal de Confirmación al Cancelar:**
- Título: "¿Descartar cambios?"
- Mensaje: "Los cambios que realizaste no se guardarán."
- Botones:
  - "Continuar editando" (volver al formulario)
  - "Descartar" (cerrar y perder cambios)

**Advertencia de Cambio de Moneda:**
- Mensaje: "⚠️ Cambiar la moneda afectará todos los precios y totales del sistema. Asegúrate de actualizar los precios de tus productos después de este cambio."
- Botones:
  - "Cancelar"
  - "Confirmar cambio"

**Advertencia de Cambio de Impuesto:**
- Mensaje: "ℹ️ El nuevo porcentaje de impuesto se aplicará a partir de la próxima venta. Las ventas anteriores mantienen el impuesto con el que fueron registradas."
- Botón: "Entendido"

### Escenarios

---
