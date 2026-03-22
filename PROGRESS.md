# PROGRESS.md

Track of implemented HUs. Read this before every session.
Update immediately after finishing each HU.

## HU Status

### Auth & Users
- [x] HU-001 — POST /auth/login
- [x] HU-002 — POST /auth/register
- [x] HU-003 — POST /auth/recover-password
- [x] HU-004 — session persistence / token refresh (frontend, backend ready)
- [x] HU-005 — roles (owner vs cashier) (frontend, backend ready)

### Dashboard
- [x] HU-006 — GET /dashboard/owner (comprehensive KPIs)
- [x] HU-007 — GET /dashboard/cashier (operational KPIs)
- [x] HU-008 — KPI calculation (implemented in dashboard service)
- [x] HU-009 — navigation & access control (role-based decorators)

### Menu
- [x] HU-010 — GET /menu/categories
- [x] HU-011 — POST /menu/categories
- [x] HU-012 — PUT /menu/categories/{id}
- [x] HU-013 — DELETE /menu/categories/{id} (soft delete)
- [x] HU-014 — GET /menu/products
- [x] HU-015 — POST /menu/products
- [x] HU-016 — PUT /menu/products/{id}
- [x] HU-017 — DELETE /menu/products/{id} (soft delete)

### Orders
- [x] HU-018 — GET /orders (list with filtering)
- [x] HU-019 — GET /orders/{id} (detail)
- [x] HU-020 — PATCH /orders/{id}/status (state change)
- [x] HU-021 — POST /orders (create order from menu)
- [x] HU-022 — PATCH /orders/{id}/notes (update notes)
- [x] HU-023 — GET /sales/history (order history with date filtering)

### POS
- [x] HU-024 — GET /pos/products (POS interface - products by category)
- [x] HU-025 — Cart logic (handled via POST /orders with items)
- [x] HU-026 — Modify quantities (frontend cart state)
- [x] HU-027 — Remove items (frontend cart state)
- [x] HU-028 — Auto-calculate totals (done in POST /orders)
- [x] HU-029 — POST /orders (payment processing - order creation)
- [x] HU-030 — Notes in order (PATCH /orders/{id}/notes)
- [x] HU-031 — Navigation (frontend)
- [x] HU-032 — GET /pos/products with is_available (product availability flag)

### Sales History
- [x] HU-033 — GET /sales/history (sales list with filtering)
- [x] HU-034 — GET /orders/{id} (sale detail - closed order)
- [x] HU-035 — Export sales to CSV (can be done frontend from /sales/history)
- [x] HU-036 — Sales analysis endpoint (GET /sales/statistics)

### Configuration
- [x] HU-037 — GET /settings (restaurant config)
- [x] HU-038 — PATCH /settings (update config)
- [x] HU-039 — Settings impact validation (applied in order creation)
- [x] HU-040 — Settings restrictions (field validations)

## Base Structure
- [x] Base project skeleton (requirements.txt, main.py, core/, dependencies.py)