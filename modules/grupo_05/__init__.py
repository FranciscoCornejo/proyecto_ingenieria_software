from flask import Blueprint, render_template

TITLE = "Grupo 05 · Funcionalidad por construir"
bp = Blueprint("grupo_05", __name__, template_folder="templates")

@bp.get("/")
def index():
    return render_template("grupo_05/index.html")
