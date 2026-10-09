"""Idempotente. Crea referencias locales sin cambiar de rama ni publicar."""
import subprocess

def git(*args):
    return subprocess.run(["git", *args], check=True)

git("rev-parse", "--verify", "main")
names = ["integracion", *[f"grupo_{n:02}" for n in range(1, 10)]]
for name in names:
    exists = subprocess.run(["git", "show-ref", "--verify", "--quiet", f"refs/heads/{name}"]).returncode == 0
    if not exists:
        git("branch", name, "main" if name == "integracion" else "integracion")
    print(f"Lista: {name}")
print("Publicar, cuando el remoto esté configurado: git push -u origin --all")
