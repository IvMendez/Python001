#Creo una funcion donde pido al usuario la base si es 10 coge por defecto la altura 3 si no se la pido al usuario 
#y muestro por pantalla el resultado
def area(base):
    if base == 10:
        altura = 3
    else:
        altura = int(input("Indica la altura del rectangulo "))
    print(f"El area seria {round(base*altura,2)}")
#Creo mi main donde pido la base y ejecuto la funcion pasandole este dato
if __name__=="__main__":
    base = int(input("Indica la base del rectangulo "))
    area(base)