"""Ejecutar: python run.py. Solo accesible desde este equipo."""
from app import create_app

if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=False)
