from flask import Blueprint, render_template

TITLE = "Grupo 02 · Funcionalidad por construir"
bp = Blueprint("grupo_02", __name__, template_folder="templates")

@bp.get("/")
def index():
    return render_template("grupo_02/index.html")
