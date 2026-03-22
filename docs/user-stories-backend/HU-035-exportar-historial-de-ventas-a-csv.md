## HU-035: Exportar Historial de Ventas a CSV

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario Owner, quiero exportar el historial de ventas a formato CSV para poder analizar los datos en Excel, hacer reportes externos o compartir información con mi contador.

### Criterios de Aceptación

**Botón Exportar CSV:**
- Ubicado en la esquina superior derecha de la página de historial
- Habilitado solo si hay ventas en el periodo filtrado

**Alcance de la Exportación:**
- Exportar todas las ventas del periodo actualmente filtrado
- Si hay filtro de fecha activo, exportar solo ese periodo
- Si hay búsqueda activa, exportar solo resultados filtrados
- Ignorar la paginación (exportar todas, no solo la página visible)

**Contenido del CSV:**
- Columnas incluidas:
  - Número de orden
  - Fecha (formato: YYYY-MM-DD)
  - Hora (formato: HH:MM)
  - Método de pago
  - Número de items
  - Subtotal
  - Impuesto
  - Total
  - Notas (si existen)
- Primera fila: Encabezados de columnas
- Datos: Una fila por venta

**Ejemplo de Contenido:**
```
Número de Orden,Fecha,Hora,Método de Pago,Items,Subtotal,Impuesto,Total,Notas
#001,2026-01-26,10:30,Efectivo,3,23.00,4.14,27.14,Sin cebolla
#002,2026-01-26,11:15,Tarjeta,5,45.00,8.10,53.10,
#003,2026-01-26,12:00,Efectivo,2,15.00,2.70,17.70,Para llevar
```

**Nombre del Archivo:**
- Formato: `ventas_[fecha_inicio]_[fecha_fin].csv`
- Si es período predefinido: `ventas_hoy.csv`, `ventas_ayer.csv`, `ventas_mes_enero.csv`
- Si es personalizado: `ventas_2026-01-01_2026-01-15.csv`
- Incluir fecha en nombre para fácil identificación

**Codificación del Archivo:**
- UTF-8 con BOM (para correcta visualización en Excel)
- Separador: Coma (,)
- Delimitador de texto: Comillas dobles (") cuando necesario
- Escape de comillas dentro del texto

**Formato de Números:**
- Usar punto (.) como separador decimal
- No usar separador de miles en el CSV
- Ejemplo: 1250.50 (no $1,250.50)

**Proceso de Descarga:**
- Descargar automáticamente al navegador

**Límites de Exportación:**
- Límite máximo: 50,000 ventas (si se excede, sugerir filtrar por periodos más cortos)

**Estados de Carga:**
- Cambiar texto a "Generando..."

**Manejo de Errores:**

**Campos con Caracteres Especiales:**
- Si las notas contienen comillas, escaparlas correctamente
- Si contienen saltos de línea, mantenerlos dentro de comillas
- Asegurar compatibilidad con Excel y Google Sheets

**Información de Periodo en el Archivo (Opcional):**
- Incluir comentario en primera línea: `# Ventas del 2026-01-01 al 2026-01-31`
- O incluir metadatos en las primeras filas antes de los datos

### Escenarios

---
