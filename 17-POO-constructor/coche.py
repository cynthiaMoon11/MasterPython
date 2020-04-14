# Definir clase

class Coche:
    color = "rojo"
    marca= "ferrari"
    modelo= "Aventador"
    velocidad=300
    caballaje=500
    plazas=2
    soyPublico ="Hola soy un atributo público"
    __soyPrivado="HOla soy un atributo privado" #un atributo privado se define con dos guiones bajos

    #contructor
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color =color
        self.marca =marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        
        



    #Métodos
    def getPrivado(self):
        return self.__soyPrivado

    def setColor(self,color):
        self.color=color
    def getColor(self):
        return self.color
    def setModelo(self,modelo):
        self.modelo=modelo
    def getModelo(self):
        return self.modelo
    def setMarca(self, marca):
        self.marca=marca
    def getMarca(self):
        return self.marca
    
    def acelerar(self):
        self.velocidad+=1
    def frenar(self):
        self.velocidad-=1
    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):

        info="____Información del Coche____"
        info+= "\n Color: "+ self.getColor()
        info+= "\n Marca: "+ self.getMarca()
        info+= "\n Modelo: "+ self.getModelo()
        info+= "\n Velocidad: "+ str(self.getVelocidad())
        info+= "\n Color: "+ self.getModelo()
        return info