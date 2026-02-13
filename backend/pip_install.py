# Run from backend folder:  python pip_install.py
# Creates venv, installs requirements, then runs the Flask app.
import os
import subprocess
import sys

BACKEND = os.path.dirname(os.path.abspath(__file__))
VENV = os.path.join(BACKEND, "venv")
IS_WIN = os.name == "nt"
VENV_PY = os.path.join(VENV, "Scripts", "python.exe") if IS_WIN else os.path.join(VENV, "bin", "python")


def main():
    os.chdir(BACKEND)
    if not os.path.isfile(VENV_PY):
        print("Creating venv...")
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    print("Installing dependencies...")
    subprocess.run([VENV_PY, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    print("Starting Flask...")
    subprocess.run([VENV_PY, "app.py"])


if __name__ == "__main__":
    main()
