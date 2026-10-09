from flask import Blueprint, render_template

TITLE = "Grupo 06 · Funcionalidad por construir"
bp = Blueprint("grupo_06", __name__, template_folder="templates")

@bp.get("/")
def index():
    return render_template("grupo_06/index.html")
