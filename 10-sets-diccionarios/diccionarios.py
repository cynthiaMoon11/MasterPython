"""
Una coleccion de datos (arrays asociativos) con un índice alfanuméricos
con formato clave valor (Json).
"""

persona={
    "nombre" :"Cynthia",
    "apellidos": "Escobar",
    "web": "cynthia.es"
}

print(type(persona))
print(persona)

print(persona["apellidos"])

#Lista con diccionarios

contactos=[
    {
        "Nombre":"Borja",
        "Apellido": "Diez"

    },
    {
        "Nombre":"Cynthia",
        "Apellido":"Escobar"
    }
]

print(contactos)
print(contactos[0]["Nombre"])

contactos[0]["Nombre"]="Borjita"
print(contactos[0]["Nombre"])

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['Nombre']}")
    print(f"Apellido del contacto: {contacto['Apellido']}")
    print("-------------------------")


