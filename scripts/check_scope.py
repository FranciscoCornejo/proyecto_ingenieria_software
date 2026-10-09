"""Comprobar rutas de un PR; ejecutar la versión confiable de la rama base."""
import re
import subprocess
import sys

def violations(branch, paths):
    if not re.fullmatch(r"grupo_0[1-9]", branch):
        raise ValueError("Para integracion la rama debe ser grupo_01 ... grupo_09")
    prefix = f"modules/{branch}/"
    return [p for p in paths if not p.startswith(prefix)]

if __name__ == "__main__":
    branch, base, head = sys.argv[1:]
    paths = subprocess.check_output(
        ["git", "diff", "--no-renames", "--name-only", "-z", f"{base}...{head}"],
    ).decode().split("\0")
    try:
        invalid = violations(branch, [p for p in paths if p])
    except ValueError as error:
        raise SystemExit(str(error))
    if invalid:
        raise SystemExit("Cambios fuera del módulo: " + ", ".join(invalid))
    print("Alcance del grupo correcto")
