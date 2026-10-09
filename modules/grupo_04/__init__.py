from flask import Blueprint, render_template

TITLE = "Grupo 04 · Funcionalidad por construir"
bp = Blueprint("grupo_04", __name__, template_folder="templates")

@bp.get("/")
def index():
    return render_template("grupo_04/index.html")
