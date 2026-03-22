## HU-001: Login de Usuario

> **Backend scope only** — UI/UX details removed.
> Implement: model → schema → service → router.


### Descripción
Como usuario registrado (Owner o Cajero), quiero iniciar sesión en el sistema para acceder a las funcionalidades del punto de venta y administración del restaurante según mi rol.

### Criterios de Aceptación

**Validaciones de Campos:**
- El campo email es requerido y debe tener formato de email válido
- El campo contraseña es requerido y debe tener mínimo 8 caracteres

**Autenticación Exitosa:**
- Guardar el token de autenticación en el cliente de forma segura
- Identificar y guardar el rol del usuario (Owner o Cajero)

**Errores de Autenticación:**
- Los mensajes de error persisten hasta que el usuario modifique algún campo o intente nuevamente

### Escenarios

1. **Login exitoso con credenciales válidas**: Usuario ingresa email y contraseña correctos, hace clic en "Iniciar Sesión", ve spinner durante 1-2 segundos, es redirigido al dashboard
2. **Email con formato inválido**: Usuario ingresa "usuario@correo" (sin dominio completo), hace clic en "Iniciar Sesión", ve mensaje de error "Ingresa un email válido"
3. **Credenciales incorrectas**: Usuario ingresa email válido pero contraseña incorrecta, hace clic en "Iniciar Sesión", ve mensaje "Email o contraseña incorrectos"

---
