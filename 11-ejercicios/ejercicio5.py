"""
tabla con info 

crear una lista que tenga esta tabla:
Accion Aventura Deportes
GTA     ASSINS  FIFA 21
COD     CRASS    PRO 21
PUGB    PRINCE      MOTO GP 21

mostrar esta informacion ordenada
"""

tabla = [
    {
        "Categoria": "Acción",
        "Juegos": ["GTA", "Call of Duty", "Pugb"]
    },
    {
        "Categoria": "Aventura",
        "Juegos": ["Assins","Crass", "Prince"]
    },
    {
        "Categoria": "Deporte",
        "Juegos": ["Fifa 21","Pro 21", "Moto Gp 21"]
    }
]

for categoria in tabla:
    print(f"------{categoria['Categoria']}--------")
    for elemento in categoria['Juegos']:
        print(elemento)
