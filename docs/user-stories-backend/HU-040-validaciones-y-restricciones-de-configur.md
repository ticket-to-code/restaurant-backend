## HU-040: Validaciones y Restricciones de Configuración

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como sistema, necesito validar la configuración del restaurante para prevenir errores y mantener la integridad de los datos en todas las operaciones.

### Criterios de Aceptación

**Validación de Nombre:**
- Frontend: Validar longitud (2-100 caracteres) antes de enviar
- Backend: Validar nuevamente longitud y que no sea solo espacios
- Trimear espacios al inicio y final
- No permitir solo espacios en blanco
- Caracteres permitidos: letras, números, espacios, guiones, paréntesis, apóstrofes

**Validación de Dirección:**
- Frontend: Validar longitud máxima (200 caracteres)
- Backend: Validar longitud máxima
- Permitir vacío (opcional)
- Trimear espacios al inicio y final
- Permitir saltos de línea (para direcciones de múltiples líneas)

**Validación de Moneda:**
- Frontend: Validar que se seleccione una opción del dropdown
- Backend: Validar que el código de moneda sea válido
- Solo permitir monedas de la lista predefinida
- No permitir valores custom o inventados
- Requerido (no puede estar vacío)

**Validación de Impuesto:**
- Frontend: Validar que sea número entre 0 y 100
- Backend: Validar rango 0-100 y formato numérico
- Permitir decimales con 1 dígito (ej: 18.5)
- No permitir valores negativos
- Redondear a 1 decimal si se ingresan más decimales
- Requerido (no puede estar vacío)

**Restricciones de Cambio de Moneda:**
- Advertir al usuario sobre el impacto antes de guardar
- Requerir confirmación explícita
- Sugerir revisar precios de productos después del cambio
- Registrar el cambio en logs de auditoría

**Restricciones de Cambio de Impuesto:**
- Informar que solo afecta nuevas ventas
- No requiere confirmación adicional (cambio menos crítico)
- Registrar el cambio en logs de auditoría

**Prevención de Configuración Incompleta:**
- No permitir dejar campos requeridos vacíos

**Validación en Backend (Crítico):**
- Nunca confiar solo en validaciones de frontend
- Validar todos los campos antes de guardar
- Retornar errores específicos si hay problemas
- Usar códigos de error estándar (400 Bad Request)

**Manejo de Valores por Defecto:**
- Si es primera configuración y el usuario no completa un campo opcional, usar valor por defecto:
  - Dirección: null o vacío
- Campos requeridos no tienen valor por defecto (usuario debe ingresarlos)

**Sanitización de Inputs:**
- Eliminar HTML/scripts si el usuario intenta inyectarlos
- Escapar caracteres especiales para prevenir XSS
- Validar que no haya código malicioso

**Consistencia de Datos:**
- Asegurar que solo haya un registro de configuración por restaurante
- Usar transacciones para garantizar atomicidad de cambios
- Prevenir condiciones de carrera si múltiples usuarios editan simultáneamente

**Mensajes de Error Específicos:**
- "El nombre es requerido"
- "El nombre debe tener entre 2 y 100 caracteres"
- "La dirección no puede exceder 200 caracteres"
- "Debes seleccionar una moneda"
- "El impuesto debe estar entre 0 y 100"
- "El impuesto debe ser un número válido"

### Escenarios

4. **Dirección excede límite**: Owner escribe 250 caracteres en dirección, ve error "La dirección no puede exceder 200 caracteres"
10. **Validación backend rechaza datos**: Owner manipula request y envía datos inválidos, el backend rechaza con error 400 y mensaje específico

---

## Resumen de Configuración Básica

**Campos de Configuración:**
- ✅ Nombre del restaurante (requerido, 2-100 caracteres)
- ✅ Dirección (opcional, máx. 200 caracteres)
- ✅ Moneda (requerido, selección de lista)
- ✅ Impuesto (requerido, 0-100%, permite decimales)

**Monedas Soportadas (Ejemplos):**
- USD - Dólar estadounidense ($)
- EUR - Euro (€)
- PEN - Sol peruano (S/)
- MXN - Peso mexicano ($)
- COP - Peso colombiano ($)
- CLP - Peso chileno ($)
- ARS - Peso argentino ($)

**Aplicación de Configuración:**
- Nombre: Tickets, facturas, header
- Dirección: Tickets, facturas
- Moneda: Todos los precios y totales del sistema
- Impuesto: Cálculo de totales en nuevas ventas

**Restricciones:**
- Solo Owner puede acceder y editar
- Primera configuración obligatoria antes de usar el sistema
- Cambios de moneda requieren confirmación
- Cambios NO afectan datos históricos

---

## Navegación en Configuración

**URLs:**
- `/settings` → Configuración del restaurante

**Breadcrumb:**
- `/settings`: Dashboard > Configuración

**Acceso:**
- Desde menú lateral: "Configuración" o "Ajustes"
- Desde perfil de usuario: Opción "Configuración"
- Primera vez: Redirección automática al crear cuenta

---

## Notas Técnicas

**Almacenamiento:**
- Tabla: `restaurant_settings` o `restaurants`
- Campos:
  - `id` (PK)
  - `restaurant_id` (FK, unique)
  - `name` (string, required)
  - `address` (text, nullable)
  - `currency_code` (string, required)
  - `tax_rate` (decimal, required)
  - `created_at` (timestamp)
  - `updated_at` (timestamp)
  - `updated_by_user_id` (FK, audit)

**Formato de Moneda:**
- Almacenar código ISO (USD, EUR, PEN)
- Tener mapeo a símbolo ($, €, S/)
- Considerar posición del símbolo (antes/después del número)
- Para USD, MXN, COP, CLP, ARS: Símbolo $ antes del número
- Para EUR: Símbolo € después del número
- Para PEN: Símbolo S/ antes del número

**Impuesto:**
- Almacenar como decimal (0.18 para 18%)
- Cálculo: subtotal × tax_rate
- Redondear resultado a 2 decimales

**Caché:**
- Cachear configuración en memoria (alta frecuencia de acceso)
- TTL: 5 minutos o invalidar al actualizar
- Evitar queries repetitivas a DB

**Validaciones:**
- Frontend: Validación inmediata en cada campo
- Backend: Validación completa antes de guardar
- Usar librería de validación (ej: Joi, Zod, Yup)

**Auditoría:**
- Registrar quién y cuándo cambió cada campo
- Tabla de historial de cambios (opcional pero recomendado)
- Útil para debugging y compliance

**Migración/Import:**
- Permitir configuración vía seed/setup inicial
- Útil para testing y demos
- Considerar import desde archivo (futuro)

**Timezone:**
- Agregar timezone como campo futuro (no MVP)
- Por ahora usar timezone del servidor o hardcoded
- Importante para cálculos de "día actual"

**Internacionalización:**
- Preparar estructura para múltiples idiomas (futuro)
- Por ahora solo español
- Nombres de monedas en español

**Seguridad:**
- Solo Owner puede modificar
- Validar permisos en cada request
- Proteger endpoints de configuración
- Registrar cambios para auditoría
