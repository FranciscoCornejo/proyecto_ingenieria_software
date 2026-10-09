from flask import Blueprint, render_template

TITLE = "Grupo 08 · Funcionalidad por construir"
bp = Blueprint("grupo_08", __name__, template_folder="templates")

@bp.get("/")
def index():
    return render_template("grupo_08/index.html")
