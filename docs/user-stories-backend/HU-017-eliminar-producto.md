## HU-017: Eliminar Producto

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción

### Criterios de Aceptación

**Trigger de Eliminación:**

**Modal de Confirmación:**
- Título: "¿Eliminar producto?"
- Mensaje: "¿Estás seguro de que deseas eliminar '[Nombre del producto]'? Este producto ya no estará disponible en el menú."
- Submensaje: "Nota: Las ventas históricas de este producto se mantendrán."
- El nombre del producto se muestra en negrita
- Botones:
  - "Cancelar" (secundario, izquierda)
  - "Eliminar" (destructivo/rojo, derecha)

**Comportamiento de Eliminación:**
- Si la eliminación es exitosa:

**Preservación de Datos Históricos:**
- La eliminación es "soft delete" (desactivación)
- Las ventas históricas que incluyen este producto se mantienen intactas
- En reportes históricos, el producto sigue apareciendo con su nombre original
- El producto simplemente deja de estar disponible para nuevas ventas

**Manejo de Errores:**

**Impacto en Categoría:**
- Al eliminar un producto, el conteo de productos de su categoría se actualiza automáticamente
- Si era el último producto de la categoría, la categoría ahora muestra "Sin productos" y puede ser eliminada

**Estado Vacío Después de Eliminar:**

**Cierre del Modal:**
- Al presionar ESC, cerrar sin eliminar

### Escenarios

---

## Resumen de Navegación en Gestión de Menú

**Breadcrumb:**
- `/menu/categorias`: Dashboard > Menú > Categorías
- `/menu/productos`: Dashboard > Menú > Productos

---

## Notas Técnicas

**Imágenes:**
- Almacenar en storage/CDN
- Generar thumbnails automáticamente (60x60, 200x200)
- Optimizar al subir (comprimir, convertir a WebP si es posible)
- Lazy loading de imágenes en la lista

**Validación de Nombres:**
- Validar unicidad case-insensitive
- Trimear espacios al inicio y final
- No permitir solo espacios

**Performance:**
- Cargar productos con paginación o virtual scrolling si hay muchos
- Caché de lista de categorías (usada en múltiples lugares)
- Optimizar queries con índices en nombre, categoría, estado

**Soft Delete:**
- Productos eliminados no se borran físicamente
- Campo deleted_at para marcar como eliminado
- Queries excluyen productos eliminados por defecto
- Mantener integridad referencial con órdenes históricas

**Estados de Producto:**
- Disponible: Activo y visible en POS
- No disponible: Existe pero no se puede vender (temporalmente agotado)
- Eliminado (soft delete): No aparece en ningún lado excepto historial

**Formatos de Moneda:**
- Usar la moneda configurada en settings
- Todos los precios en formato consistente
- Validar que precio > 0
