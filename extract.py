#!/usr/bin/env python3
"""
Extract backend-relevant content from HU markdown files.
Usage: python extract_backend.py
Reads  docs/user-stories/HU-*.md
Writes docs/user-stories-backend/HU-*.md
"""

import re
from pathlib import Path

INPUT_DIR  = Path("docs/user-stories")
OUTPUT_DIR = Path("docs/user-stories-backend")

# Bold sub-headings that are 100% frontend — drop the heading AND its bullets
SKIP_BOLD_SECTIONS = [
    "estructura", "contenido de la pantalla", "estado del botón", "estado del boton",
    "interacción con contraseña", "interaccion con contrasena",
    "navegación", "navegacion", "diseño", "layout", "visual", "ui ",
    "feedback", "skeleton", "animaci", "responsive", "apariencia",
]

# Individual bullet keywords → drop that bullet
SKIP_LINE_KW = [
    "mostrar", "ocultar", "spinner", "placeholder", "color rojo", "color ",
    "icono", "ícono", "redirigir", "redirige", "pantalla", "layout",
    "animaci", "skeleton", "tooltip", "toast", "modal",
    "diseño", "fuente", "estilo", "css", "viewport",
    "responsive", "tablet", "móvil", "movil",
    "clic en ", "hacer clic", "al hacer clic",
    "botón ", "boton ", "link ", "href",
    "texto cambia", "deshabilita", "habilita el botón",
    "puntos/asteriscos", "texto plano",
    "logo ", "título ", "titulo ", "formulario centrado",
]

# Scenario bullets — keep only those with backend signals
KEEP_SCENARIO_KW = [
    "exitoso", "válido", "invalido", "inválido", "incorrecto", "incorrectos",
    "credencial", "token", "rol ", "permiso", "duplicado", "existe",
    "no existe", "expirado", "límite", "limite", "bloqueo", "bloqueado",
    "409", "401", "403", "404", "400", "500", "error de autenticación",
    "contraseña incorrecta", "email no existe", "cuenta bloqueada",
    "registro exitoso", "datos inválidos", "ya registrado",
]


def skip_bold_section(line: str) -> bool:
    m = re.match(r"\*\*(.+?)\*\*", line.strip())
    if not m:
        return False
    return any(kw in m.group(1).lower() for kw in SKIP_BOLD_SECTIONS)


def skip_line(line: str) -> bool:
    l = line.lower()
    return any(kw in l for kw in SKIP_LINE_KW)


def keep_scenario(line: str) -> bool:
    l = line.lower()
    return any(kw in l for kw in KEEP_SCENARIO_KW)


def extract(text: str) -> str:
    lines = text.splitlines()
    out = []
    in_scenarios = False
    skip_bold = False   # currently inside a skipped bold sub-section

    for line in lines:
        stripped = line.strip()

        # Detect ### section
        if stripped.startswith("### "):
            in_scenarios = "escenario" in stripped.lower()
            skip_bold = False
            out.append(line)
            continue

        # Detect bold sub-heading (e.g. **Estructura y Contenido de la Pantalla:**)
        if re.match(r"\*\*.+\*\*:?\s*$", stripped):
            if skip_bold_section(line):
                skip_bold = True
                continue
            else:
                skip_bold = False
                out.append(line)
                continue

        # If inside a skipped bold section, drop lines until next bold heading or blank+non-bullet
        if skip_bold:
            if stripped == "" or (not stripped.startswith("-") and not stripped.startswith("*") and not stripped.startswith(" ")):
                skip_bold = False
                # don't append this line yet — re-evaluate
            else:
                continue

        # Scenario bullets
        if in_scenarios and re.match(r"\d+\.", stripped):
            if keep_scenario(line):
                out.append(line)
            continue

        # Generic bullet filter
        if skip_line(line):
            continue

        out.append(line)

    # Collapse multiple blank lines
    result, blanks = [], 0
    for line in out:
        if line.strip() == "":
            blanks += 1
            if blanks == 1:
                result.append("")
        else:
            blanks = 0
            result.append(line)

    return "\n".join(result).strip() + "\n"


HEADER_NOTE = (
    "> **Backend scope only** — UI/UX details removed.\n"
    "> Implement: model → schema → service → router.\n\n"
)


def process_file(src: Path, dst: Path):
    original = src.read_text(encoding="utf-8")
    cleaned  = extract(original)

    # Insert note after ## HU-XXX line
    lines = cleaned.splitlines(keepends=True)
    for i, l in enumerate(lines):
        if l.startswith("## HU-"):
            lines.insert(i + 1, "\n" + HEADER_NOTE)
            break
    final = "".join(lines)

    dst.write_text(final, encoding="utf-8")
    orig_n = len(original.splitlines())
    new_n  = len(final.splitlines())
    pct    = 100 - int(new_n * 100 / orig_n)
    return orig_n, new_n, pct


def main():
    files = sorted(INPUT_DIR.glob("HU-*.md"))
    if not files:
        print(f"❌  No HU files in {INPUT_DIR}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📂  {INPUT_DIR}  →  {OUTPUT_DIR}\n")

    total_orig = total_new = 0
    for f in files:
        o, n, pct = process_file(f, OUTPUT_DIR / f.name)
        total_orig += o
        total_new  += n
        bar = "█" * (pct // 10) + "░" * (10 - pct // 10)
        print(f"  {f.name:45s}  {o:3d} → {n:3d} lines  [{bar}] -{pct}%")

    overall = 100 - int(total_new * 100 / total_orig)
    print(f"\n✅  {len(files)} files  |  {total_orig} → {total_new} total lines  (-{overall}% overall)")
    print(f"    Files saved to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()