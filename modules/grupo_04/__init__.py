from flask import Blueprint, render_template, request
from . import logic

TITLE = "Grupo 04 · Funcionalidad por construir"
bp = Blueprint("grupo_04", __name__, template_folder="templates")


@bp.get("/")
def index():
    return render_template("grupo_04/index.html")


@bp.get("/calcular-cupos")
def calcular():
    try:
        capacidad_total = request.args.get("capacidad_total", type=int)
        cupos_ocupados = request.args.get("cupos_ocupados", type=int)

        if capacidad_total is None or cupos_ocupados is None:
            raise ValueError("Debes ingresar la capacidad total y los cupos ocupados.")

        cupos_disponibles = logic.calcular_cupos_disponibles(capacidad_total, cupos_ocupados)

        return render_template(
            "grupo_04/index.html",
            resultado=cupos_disponibles
        )

    except ValueError as error:
        return render_template(
            "grupo_04/index.html",
            error=str(error)
        ), 400