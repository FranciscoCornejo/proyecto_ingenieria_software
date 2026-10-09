from flask import Blueprint, render_template

TITLE = "Grupo 01 · Funcionalidad por construir"
bp = Blueprint("grupo_01", __name__, template_folder="templates")

@bp.get("/")
def index():
    return render_template("grupo_01/index.html")
