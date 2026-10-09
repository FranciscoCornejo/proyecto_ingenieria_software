from flask import Blueprint, render_template, request
from .logic import kilometers_to_meters

TITLE = "Ejemplo docente · Kilómetros a metros"
bp = Blueprint("ejemplo", __name__, template_folder="templates")

@bp.get("/")
def index():
    value = request.args.get("km", "")
    result, error = None, None
    if "km" in request.args:
        try:
            result = kilometers_to_meters(value)
        except ValueError as exception:
            error = str(exception)
    return render_template("ejemplo/index.html", value=value, result=result, error=error), (400 if error else 200)
