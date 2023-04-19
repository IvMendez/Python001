#Añado una lista con los diferente numeros positivos y negativos
lista = [5, 3, 12, -6, -3, 1, 6, 8, -12]
#Creo una funcion donde recorro la lista entera si es un numero positivo lo muestro por pantalla y si es el 6 lo saludo
def imprimir():
    for i in lista:
        if i > 0:
            print(i)
        if i == 6:
            print("Hola número 6")
#Creo mi main donde ejecuto mi funcion
if __name__=="__main__":
    imprimir()