"""Núcleo docente: descubre módulos y construye el portal local."""
from importlib import import_module
from pathlib import Path
from flask import Blueprint, Flask, render_template

def create_app():
    app = Flask(__name__)
    modules = []
    root = Path(__file__).parent / "modules"
    for folder in sorted(root.iterdir()):
        if not folder.is_dir() or not (folder / "__init__.py").is_file():
            continue
        if folder.name not in ["ejemplo", *[f"grupo_{n:02}" for n in range(1, 10)]]:
            continue
        module = import_module(f"modules.{folder.name}")
        if not isinstance(module.bp, Blueprint) or module.bp.name != folder.name:
            raise ValueError(f"El Blueprint debe llamarse {folder.name}")
        if module.bp.url_prefix is not None:
            raise ValueError("El prefijo lo define el núcleo")
        app.register_blueprint(module.bp, url_prefix=f"/modulos/{folder.name}")
        modules.append({"id": folder.name, "title": module.TITLE})

    @app.get("/")
    def index():
        return render_template("index.html", modules=modules)

    return app
