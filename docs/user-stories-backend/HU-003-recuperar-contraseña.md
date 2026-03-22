## HU-003: Recuperar Contraseña

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario registrado que olvidó su contraseña, quiero poder restablecerla mediante mi correo electrónico para poder volver a acceder al sistema.

### Criterios de Aceptación

**Validaciones de Campos:**
- El campo email es requerido
- El campo email debe tener formato válido

**Envío Exitoso:**
- El mensaje de éxito se muestra en un banner verde en la parte superior del formulario
- El formulario permanece visible para permitir reintentos

**Manejo de Errores:**

**Link de Recuperación (Email):**
- El email recibido contiene:
  - Asunto: "Recuperación de contraseña - [Nombre App]"
  - Mensaje personalizado con nombre del restaurante si está disponible
  - Mensaje de seguridad: "Si no solicitaste este cambio, ignora este email"

**Página de Restablecer Contraseña:**

**Validaciones en Página de Restablecimiento:**
- Nueva contraseña: mínimo 8 caracteres, debe contener al menos una letra y un número
- Confirmar nueva contraseña: debe coincidir exactamente con nueva contraseña
- Los mensajes de error son los mismos que en la página de registro

**Restablecimiento Exitoso:**

**Tokens Inválidos o Expirados:**

### Escenarios

2. **Email no registrado en sistema**: Usuario ingresa email que no existe, hace clic en "Enviar link", ve el mismo mensaje de éxito (por seguridad), pero no recibe email
3. **Email con formato inválido**: Usuario ingresa "usuario@" (incompleto), intenta enviar, ve mensaje "Ingresa un email válido"
5. **Error de conexión al enviar**: Usuario ingresa email válido pero hay error de red, ve mensaje "No se pudo enviar el email. Por favor, intenta de nuevo"
6. **Restablecimiento exitoso**: Usuario recibe email, hace clic en link, ingresa "NewPass123" en ambos campos, hace clic en "Restablecer contraseña", ve mensaje de éxito, es redirigido a login después de 2 segundos
9. **Token expirado**: Usuario hace clic en link de recuperación después de 2 horas, ve mensaje "Este link de recuperación ha expirado. Por favor, solicita uno nuevo" con botón para solicitar nuevo link
10. **Token inválido o ya usado**: Usuario intenta usar el mismo link dos veces, la segunda vez ve mensaje "Este link de recuperación no es válido o ya fue usado"
11. **Reenvío de email de recuperación**: Usuario solicita recuperación, espera y no ve el email, vuelve a `/recuperar-password`, ingresa email nuevamente, recibe nuevo email con nuevo token

---
