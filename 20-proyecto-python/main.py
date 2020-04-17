"""
Proyecto MySql y python
-abrir asistente
-login
-registrar
-login
-crea, muestra y elimina una nota
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -Registro
    -Login
""")

hazEl= acciones.Acciones()

accion = input("¿Qué quieres hacer?:")

if accion=="registro":
    hazEl.registro()

elif accion=="loging":
    hazEl.login()
    