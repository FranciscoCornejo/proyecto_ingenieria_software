from flask import Blueprint, render_template

TITLE = "Grupo 07 · Funcionalidad por construir"
bp = Blueprint("grupo_07", __name__, template_folder="templates")

@bp.get("/")
def index():
    return render_template("grupo_07/index.html")
