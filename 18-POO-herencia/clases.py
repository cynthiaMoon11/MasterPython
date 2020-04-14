class Persona:

    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad
     
    def setNombre(self, nombre):
        self.nombre =nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura=altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar (self):
        return "Estoy hablando"
    
    def caminar (self):
        return "Estoy camiando"
    
    def dormir (self):
        return "Estoy durmiendo"

class Informatico (Persona):
        
    def __init__(self):
            self.lenguajes ="Html , CSS, JavaScrip , PHP"
            self.experiencia=5
        
    def getLenguajes (self):
            return self.lenguajes
        
    def aprender(self, lenguajes):
            self.lenguajes = lenguajes
            return self.lenguajes
        
    def programar(self):
            return "Estoy programando"
        
    def repararPc(self):
            return "estoy reparando pc"

class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__() #se accede al constructor de la clase padre
        self.auditarRedes="experto"
        self.experienciaRedes = 15
        
    def auditoria(self):
        return "estoy auditando"
