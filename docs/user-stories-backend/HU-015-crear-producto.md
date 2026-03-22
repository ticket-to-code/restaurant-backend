## HU-015: Crear Producto

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero crear nuevos productos para ampliar el menú del restaurante y poder ofrecerlos a los clientes en el punto de venta.

### Criterios de Aceptación

**Trigger del Modal:**

**Campo Imagen (opcional):**
- Área de carga de imagen con texto: "Arrastra una imagen o haz clic para seleccionar"
- Preview de la imagen seleccionada (máximo 200x200px)
- Formatos aceptados: JPG, PNG, WebP
- Tamaño máximo: 5MB

**Campo Nombre (requerido):**
- Label: "Nombre del producto *"
- Mínimo 2 caracteres, máximo 100 caracteres
- Error si vacío: "El nombre es requerido"
- Error si < 2 caracteres: "El nombre debe tener al menos 2 caracteres"

**Campo Categoría (requerido):**
- Label: "Categoría *"
- Dropdown con lista de categorías activas del sistema
- Error si no se selecciona: "La categoría es requerida"

**Campo Precio (requerido):**
- Label: "Precio *"
- Input numérico con símbolo de moneda (ej: "$")
- Acepta decimales (2 dígitos después del punto)
- Mínimo: 0.01 (debe ser mayor a 0)
- Máximo: 999999.99
- Error si vacío o 0: "El precio es requerido y debe ser mayor a 0"
- Error si excede máximo: "El precio no puede superar $999,999.99"
- Formatear automáticamente mientras escribe (ej: "1250" → "1,250.00")

**Campo Descripción (opcional):**
- Label: "Descripción"
- Textarea de 3-4 líneas
- Máximo 500 caracteres
- Error si excede: "La descripción no puede superar 500 caracteres"

**Estado Inicial del Producto:**
- Al crear, el producto se crea automáticamente con estado "Disponible"
- No hay opción de elegir el estado inicial

**Validación de Campos Requeridos:**
- Visual: campos requeridos marcados con asterisco (*)

**Comportamiento del Botón Crear:**

**Creación Exitosa:**
- Agregar el nuevo producto a la lista

**Manejo de Errores:**

**Carga de Imagen:**

**Cierre del Modal:**
- Al presionar ESC, cerrar sin guardar

**Creación Rápida de Categoría:**

### Escenarios

8. **Contador de caracteres en descripción**: Owner escribe en descripción, ve contador actualizar "45/500 caracteres"
9. **Descripción excede límite**: Owner escribe 550 caracteres, ve error "La descripción no puede superar 500 caracteres"
11. **Formato de imagen inválido**: Owner intenta cargar archivo .gif, ve error "Solo se aceptan imágenes JPG, PNG o WebP"
14. **Nombre duplicado**: Ya existe "Coca Cola", Owner intenta crear otro "Coca Cola", ve error "Ya existe un producto con este nombre"

---
