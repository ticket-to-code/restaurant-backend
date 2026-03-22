## HU-016: Editar Producto

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero editar los productos existentes para actualizar precios, cambiar información, o corregir errores en el menú.

### Criterios de Aceptación

**Trigger del Modal:**

**Campos Precargados:**
- Nombre: Precargado con valor actual, texto seleccionado
- Categoría: Dropdown con categoría actual seleccionada
- Precio: Precargado con precio actual formateado
- Descripción: Precargada con descripción actual (o vacía si no tiene)

**Validaciones:**
- Las mismas validaciones que en creación
- Permitir guardar si el nombre es igual al actual (sin cambios)

**Cambio de Imagen:**
- Preview de la nueva imagen seleccionada
- Opción "Eliminar imagen" para quitar la imagen actual (producto quedará sin imagen)

**Detección de Cambios:**

**Comportamiento del Botón Guardar:**

**Edición Exitosa:**
- Actualizar la fila correspondiente en la lista con los nuevos datos
- Mantener el orden y filtros aplicados

**Cambio de Categoría:**
- Permitir cambiar el producto de categoría
- Si hay filtro activo por la categoría anterior, el producto desaparece de la vista
- El producto ahora pertenece a la nueva categoría

**Manejo de Errores:**

**Cierre del Modal:**
- Al presionar ESC, cerrar sin guardar

**Preservación de Datos:**
- Al editar, se mantiene:
  - El estado del producto (Disponible/No disponible)
  - El ID único del producto
  - Las ventas históricas asociadas

### Escenarios

7. **Validar nombre duplicado**: Owner edita "Tacos" e intenta cambiarlo a "Burritos" (que ya existe), ve error "Ya existe un producto con este nombre"

---
