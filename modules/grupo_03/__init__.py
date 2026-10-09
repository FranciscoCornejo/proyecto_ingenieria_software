from flask import Blueprint, render_template

TITLE = "Grupo 03 · Funcionalidad por construir"
bp = Blueprint("grupo_03", __name__, template_folder="templates")

@bp.get("/")
def index():
    return render_template("grupo_03/index.html")
