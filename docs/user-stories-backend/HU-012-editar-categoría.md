## HU-012: Editar Categoría

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero editar el nombre de una categoría existente para corregir errores o actualizar la nomenclatura del menú.

### Criterios de Aceptación

**Trigger del Modal:**

**Campo Nombre Precargado:**
- El campo muestra el nombre actual de la categoría
- El texto está seleccionado automáticamente para facilitar el reemplazo
- Las validaciones son las mismas que en creación:
  - Requerido
  - Mínimo 2 caracteres, máximo 50 caracteres
  - No puede ser igual a otra categoría existente (excepto la actual)

**Validaciones:**
- Si el nombre es idéntico al actual, permitir guardar (sin cambios)

**Detección de Cambios:**

**Comportamiento del Botón Guardar:**

**Edición Exitosa:**
- Actualizar la fila correspondiente en la lista con el nuevo nombre
- Mantener el orden alfabético de la lista

**Manejo de Errores:**
- Mantener el valor editado en el campo

**Cierre del Modal:**
- Al presionar tecla ESC, cerrar sin guardar

**Preservación de Datos:**
- Al editar el nombre, se mantienen:
  - El estado de la categoría (Activa/Inactiva)
  - Los productos asociados a la categoría
  - El ID único de la categoría

### Escenarios

4. **Validar nombre duplicado**: Existen "Bebidas" y "Postres", Owner edita "Postres" e intenta cambiarlo a "Bebidas", ve error "Ya existe una categoría con este nombre"
6. **Mantener orden alfabético**: Existen "Bebidas", "Entradas", "Postres", Owner edita "Postres" a "Sopas", al guardar la lista se reordena: "Bebidas", "Entradas", "Sopas"

---
