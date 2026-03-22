## HU-028: Cálculo Automático de Totales

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero que el sistema calcule automáticamente los totales de la orden incluyendo impuestos para tener el monto exacto a cobrar sin hacer cálculos manuales.

### Criterios de Aceptación

**Componentes del Cálculo:**
- Subtotal: Suma de (precio unitario × cantidad) de todos los productos
- Impuesto: Subtotal × (porcentaje de impuesto configurado)
- Total: Subtotal + Impuesto

**Porcentaje de Impuesto:**
- Usar el porcentaje configurado en `/settings` del restaurante
- Si no está configurado, usar 0% por defecto
- El porcentaje se aplica sobre el subtotal

**Formato de Moneda:**
- Usar el símbolo de moneda configurado en settings (ej: "$", "€", "S/")
- Formato con separador de miles y 2 decimales obligatorios
- Ejemplos: "$1,250.50", "€45.00", "S/123.75"

**Actualización Automática:**
- Los totales se recalculan inmediatamente cuando:
  - Se agrega un producto
  - Se cambia cantidad de un producto
  - Se elimina un producto
  - Se limpia el carrito

**Precisión de Cálculos:**
- Usar aritmética de punto flotante adecuada para dinero
- Redondear impuesto y total a 2 decimales
- Asegurar que la suma sea exacta (subtotal + impuesto = total)

**Carrito Vacío:**
  - "Subtotal: $0.00"
  - "IVA (18%): $0.00"
  - "Total: $0.00"

**Ejemplo de Cálculo:**
- Producto 1: Hamburguesa × 2 = $20.00
- Producto 2: Coca Cola × 3 = $9.00
- Subtotal: $29.00
- IVA (18%): $5.22
- Total: $34.22

**Validación de Consistencia:**
- El total guardado en la orden debe ser idéntico al calculado en el POS

### Escenarios

---
