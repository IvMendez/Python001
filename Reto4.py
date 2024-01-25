#Reto 4

#Un juego para que el usuario adivine un numero
import random

x = random.randint(1,100)#Generamos un numero aleatorio entre 1 y 100
intentos = 0#Creamos el numero de intentos
print("Intenta adivinar en que numero estoy pensando, es un numero del 1 al 100")
while True:
    eleccion = int(input("Que numero crees que es?: "))#Le pedimos al usuario que nos diga que numero cree que es
    if eleccion==x:
        print(f"Bien lo has adivinado , el numero es {x}")#Le indicamos si el numero es correcto o en su defecto si es mayor o menor del numero generado
        break
    elif eleccion>x and eleccion<=100:
        print("Es un numero menor")
        intentos+=1
    elif eleccion<x and eleccion >=0:
        print("Es un numero mayor")
        intentos+=1
    else:
        print("Ese numero esta no entre 1 y 100")
        intentos+=1
print(f"Solo has necesitado {intentos} intentos")#Contamos los intentos y se los indicamos al usuario
