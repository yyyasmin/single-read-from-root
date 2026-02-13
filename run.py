# Run backend + frontend from project root:  python run.py
import os
import sys
import subprocess
import platform

ROOT = os.path.dirname(os.path.abspath(__file__))
BACKEND = os.path.join(ROOT, "backend")
FRONTEND = os.path.join(ROOT, "frontend")
VENV = os.path.join(BACKEND, "venv")
IS_WIN = platform.system() == "Windows"
VENV_PY = os.path.join(VENV, "Scripts", "python.exe") if IS_WIN else os.path.join(VENV, "bin", "python")
VENV_PIP = os.path.join(VENV, "Scripts", "pip.exe") if IS_WIN else os.path.join(VENV, "bin", "pip")


def run(cmd, cwd=None, shell=None):
    if shell is None:
        shell = IS_WIN
    return subprocess.run(cmd, cwd=cwd or ROOT, shell=shell)


def main():
    os.chdir(ROOT)

    # Backend: ensure venv and deps
    if not os.path.isfile(VENV_PY):
        print("Creating backend venv...")
        run([sys.executable, "-m", "venv", VENV])
    print("Installing backend dependencies...")
    run([VENV_PY, "-m", "pip", "install", "-r", "requirements.txt"], cwd=BACKEND)

    # Frontend: npm install
    print("Installing frontend dependencies...")
    run("npm install", cwd=FRONTEND)

    # Start both servers
    print("Starting backend (Flask) on http://localhost:5000 ...")
    print("Starting frontend (Vite) on http://localhost:3000 ...")
    print("Press Ctrl+C to stop both.\n")
    backend_proc = subprocess.Popen(
        [VENV_PY, "app.py"],
        cwd=BACKEND,
    )
    frontend_proc = subprocess.Popen(
        "npm start",
        cwd=FRONTEND,
        shell=True,
    )
    try:
        frontend_proc.wait()
    except KeyboardInterrupt:
        pass
    finally:
        backend_proc.terminate()
        frontend_proc.terminate()
        print("\nStopped.")


if __name__ == "__main__":
    main()
