from flask import Blueprint, render_template

TITLE = "Grupo 09 · Funcionalidad por construir"
bp = Blueprint("grupo_09", __name__, template_folder="templates")

@bp.get("/")
def index():
    return render_template("grupo_09/index.html")
