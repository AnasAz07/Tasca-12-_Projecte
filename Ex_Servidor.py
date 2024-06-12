import subprocess

def iniciar_servidor_django():
    try:
        subprocess.run(["python3", "Server_Django/mysite/manage.py", "runserver", "8082"], check=True)
    except subprocess.CalledProcessError as e:
        print("Error al iniciar el servidor Django:", e)

