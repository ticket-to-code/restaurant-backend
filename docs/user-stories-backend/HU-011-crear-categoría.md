## HU-011: Crear Categoría

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero crear nuevas categorías para organizar los productos del menú de manera lógica y facilitar la navegación en el punto de venta.

### Criterios de Aceptación

**Trigger del Modal:**

**Campo Nombre:**
- Label: "Nombre de la categoría"
- Requerido (marcado con asterisco *)
- Mínimo 2 caracteres, máximo 50 caracteres
- Permite letras, números, espacios, y algunos caracteres especiales (guion, paréntesis)

**Validaciones:**

**Estado Inicial de la Categoría:**
- Al crear, la categoría se crea automáticamente con estado "Activa"
- No hay opción de elegir el estado inicial (siempre Activa por defecto)

**Comportamiento del Botón Crear:**

**Creación Exitosa:**
- Actualizar la lista de categorías mostrando la nueva categoría
- La nueva categoría aparece en la lista ordenada alfabéticamente

**Manejo de Errores:**
- Mantener el valor ingresado en el campo

**Cierre del Modal:**
- Al presionar tecla ESC, cerrar sin guardar

**Focus y UX:**

### Escenarios

5. **Nombre duplicado**: Ya existe categoría "Bebidas", Owner intenta crear otra "bebidas" (minúsculas), ve error "Ya existe una categoría con este nombre"
14. **Nueva categoría aparece ordenada**: Existen categorías "Bebidas" y "Postres", Owner crea "Entradas", al cerrar el modal la lista muestra: "Bebidas", "Entradas", "Postres" (orden alfabético)

---
