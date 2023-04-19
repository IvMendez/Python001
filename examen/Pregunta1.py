#Creo la clase animal con sus atributos
class Animal:
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas
#Creo las clases hijas perro y pajaro que heredan de esta ampliando atributos y creando sus metodos
class Perro(Animal):
    def __init__(self,nombre,patas,raza):
        super().__init__(nombre,patas)
        self.raza = raza
    def hacerRuido(self):
        print("Woof, woof")
    def correr(self):
        return "Esta corriendo"
class Pajaro(Animal):
    def __init__(self, nombre, patas):
        super().__init__(nombre, patas)
    def hacerRuido(self):
        print("Tweet, tweet")
    def volar(self):
        pass
#Creo la funcion que me permte crear 3 animales del tipo que yo quiera para ver su funcionalidad
def crearAnimales():
    for i in range(0,3):
        nombre = input("Escribe el nombre del animal ")
        patas = int(input("Indica el número de patas "))
        animal = Animal(nombre, patas)
        r = input(f"{animal.nombre} es un perro o un pajaro? ")
        if r.upper() == "PERRO":
           raza = input("Indica de que raza es? ")
           perro = Perro(nombre, patas ,raza)
           print(f"el perro se llama {perro.nombre}, tiene {perro.patas} patas")
           perro.hacerRuido()
           print(f"{perro.nombre} {perro.correr()}")
        if r.upper() == "PAJARO":
           pajaro = Pajaro(nombre, patas)
           print(f"el pajaro se llama {pajaro.nombre}, tiene {pajaro.patas} patas")
           pajaro.hacerRuido()
#hago una funcion que me permite crear un perro y ver sus metodos en accion
def crearPerro():
    nombre = input("Escribe el nombre del perro ")
    patas = int(input("Indica el número de patas "))
    raza = input("Indica de que raza es? ")
    perro = Perro(nombre, patas ,raza)
    perro.hacerRuido()
    print(f"{perro.nombre} {perro.correr()}") 
#Creo un main donde ejecuto mis funciones        
if __name__=="__main__":
    crearAnimales()
    crearPerro()