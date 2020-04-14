"""
POO
clase, molde
"""
# Definir clase

class Coche:
    color = "rojo"
    marca= "ferrari"
    modelo= "Aventador"
    velocidad=300
    caballaje=500
    plazas=2

    #Métodos
    def setColor(self,color):
        self.color=color
    def getColor(self):
        return self.color
    def setModelo(self,modelo):
        self.modelo=modelo
    def getModelo(self):
        return self.modelo
    def acelerar(self):
        self.velocidad+=1
    def frenar(self):
        self.velocidad-=1
    def getVelocidad(self):
        return self.velocidad
    

#instanciar la clase (crear objeto)
coche = Coche()

print("Velocidad: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad: ", coche.getVelocidad())

coche.setColor("amarillo")
coche.setModelo("Murcielago")

print(coche.getColor())
print(coche.getModelo())

#Crear mas objetos

coche2 = Coche()
coche2.setModelo("Verde")
coche2.setModelo("Gallardo")
print("Color del Coche 2:  ", coche2.getColor())
print("modelo del Coche 2:  ", coche2.getModelo())

print(coche.getColor())
print(coche.getModelo())





