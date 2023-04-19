#Creo una funcion donde recibo el area y la altura  por defecto en 3 e imprimo la operacion
def area(base, altura = 3):
    print(f"El area seria {round(base*altura,2)}")
#Creo mi main donde pido la base y la altura y no me dan la altura cojo la que esta  por defecto y si no paso ambos datos
if __name__=="__main__":
    base = int(input("Indica la base del rectangulo "))
    altura = input("Indica la altura del rectangulo ")
    if altura != "":
        altura =int(altura)
    if type(altura) == str:
        area(base)
    else:
        area(base,altura)