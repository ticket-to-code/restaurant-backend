## HU-002: Registro de Restaurante

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como nuevo usuario, quiero registrar mi restaurante en el sistema para poder empezar a usar el punto de venta y las funcionalidades de administración.

### Criterios de Aceptación

**Validaciones de Campos:**
- Nombre del restaurante: requerido, mínimo 3 caracteres, máximo 100 caracteres
- Tu nombre completo: requerido, mínimo 3 caracteres, máximo 100 caracteres
- Correo electrónico: requerido, formato de email válido
- Contraseña: requerida, mínimo 8 caracteres, debe contener al menos una letra y un número
- Confirmar contraseña: requerida, debe coincidir exactamente con el campo "Contraseña"
- Dirección: opcional, máximo 200 caracteres
- Checkbox términos: debe estar marcado para poder continuar

**Mensajes de Error Específicos:**
- Si nombre del restaurante < 3 caracteres: "El nombre debe tener al menos 3 caracteres"
- Si nombre completo < 3 caracteres: "El nombre debe tener al menos 3 caracteres"
- Si email es inválido: "Ingresa un email válido"
- Si email ya está registrado: "Este email ya está en uso. Por favor, usa otro email o inicia sesión"
- Si contraseña < 8 caracteres: "La contraseña debe tener al menos 8 caracteres"
- Si contraseña no contiene letra y número: "La contraseña debe contener al menos una letra y un número"
- Si confirmar contraseña no coincide: "Las contraseñas no coinciden"
- Si checkbox no está marcado: "Debes aceptar los términos y condiciones"

**Registro Exitoso:**
- Si el registro es exitoso, crear automáticamente:
  - Una cuenta con el email proporcionado
  - Un restaurante con el nombre proporcionado
  - Una sucursal por defecto asociada al restaurante
  - Asignar rol "Owner" al usuario

**Campos con Mostrar/Ocultar Contraseña:**

**Términos y Condiciones:**
- El checkbox permanece desmarcado por defecto

### Escenarios

1. **Registro exitoso con datos válidos**: Usuario completa todos los campos correctamente, marca términos, hace clic en "Crear cuenta", ve spinner, es redirigido al dashboard con mensaje de bienvenida
2. **Email ya registrado**: Usuario intenta registrarse con un email que ya existe en el sistema, ve mensaje "Este email ya está en uso. Por favor, usa otro email o inicia sesión"

---
