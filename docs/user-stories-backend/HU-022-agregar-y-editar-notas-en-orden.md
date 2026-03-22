## HU-022: Agregar y Editar Notas en Orden

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario (Owner o Cajero), quiero agregar o editar notas en una orden para comunicar instrucciones especiales o información relevante sobre el pedido.

### Criterios de Aceptación

**Agregar Notas al Crear Orden:**
- Durante la creación de orden (en POS o mini-POS), incluir campo opcional "Notas"
- Textarea de 2-3 líneas
- Máximo 500 caracteres
- Contador de caracteres: "0/500"
- Las notas se guardan al crear la orden

**Editar Notas en Detalle de Orden:**
- Solo permitir editar notas si la orden NO está Cerrada

**Botón Agregar Notas:**
- Botones: "Cancelar" (secundario) y "Guardar" (primario)

**Edición de Notas Existentes:**
- Permitir modificar o borrar todo el contenido

**Validaciones:**
- Máximo 500 caracteres
- Permitir guardar notas vacías (equivalente a eliminar notas)

**Guardar Notas:**
- Si es exitoso:
- Si hay error:
  - Mantener textarea editable con el contenido

**Cancelar Edición:**

**Restricción en Órdenes Cerradas:**

**Indicador de Notas en Lista:**

**Formato de Notas:**
- Mantener saltos de línea si el usuario los ingresa
- Trimear espacios al inicio y final
- No permitir solo espacios en blanco

### Escenarios

4. **Editar notas existentes**: Usuario abre orden con notas "Sin cebolla", hace clic en área de notas, edita a "Sin cebolla, sin tomate", hace clic en "Guardar cambios", las notas se actualizan
7. **Validación de máximo caracteres**: Usuario intenta escribir 550 caracteres en notas, al llegar a 500 se detiene la escritura o ve error "Las notas no pueden superar 500 caracteres"
8. **Contador de caracteres**: Usuario escribe notas, ve contador actualizar "45/500 caracteres"

---
