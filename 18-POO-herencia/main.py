"""
herencia: psibilidad de compartir atributos y métodos
"""

#importar todo el archivo donde estan las clases
import clases

persona = clases.Persona()
persona.setNombre("Cynthia")
persona.setApellidos("Escobar Luna")
persona.setAltura(168)
persona.setEdad(30)

print(f"Eres, {persona.getNombre()} {persona.getApellidos()} y tienes {persona.getEdad()} mides {persona.getAltura()}")
print(persona.hablar())

#creamos un objeto informatico

informatico=clases.Informatico()
informatico.setNombre("Rafael")
informatico.setApellidos("Chamon")
informatico.setEdad(28)
#informatico.Lenguajes("css, jS, python")
#informatico.Experiencia(2)
informatico.aprender("CSS, Python, PHP, ORACLE")

print(informatico.getLenguajes())

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Cynthia")
print(f"Eres, {tecnico.getNombre()}")
print(f"saber, {tecnico.getLenguajes()}")


