#RETO 2

#Introducir las edades de los usuarios y validar los que estan entre 18 y 65 x veces

edades = []#Creamos una lista con las edades que vamos a ir poniendo
nombres = []#Creamos una lista con las edades que vamos a ir poniendo
personas = 0#Creamos una variable para contar el numero de personas que se introducen
while True:
    pregunta = input("Quieres incluir un nuevo usuario (s,n)? ")#Creamos un bucle y preguntamos al usuario si va a querer incluir un nuevo usuario
    if pregunta == "s" or pregunta == "S":
        nombre = input("Introduce el nombre del trabajador ")#Introducimos el nombre del usuario
        edad = int(input("Introduce la edad del trabajador "))#Introducimos la edad del usuario
        if edad >= 18 and edad <= 65:#Validamos la edad
            edades.append(edad)#Si es valido ponemos la edad en la lista de edad y el nombre a la lista de nombres y sumamos 1 a personas
            nombres.append(nombre)
            personas+=1
        else:
            print("Edad fuera de rango (18-65)")
    elif pregunta == "n" or pregunta == "N":#Si no queremos añadir a nadie mas mostramos ambas listas para que nos aparezcan los usuarios regitrados y sus edades
        for i in range(personas):
            print(nombres[i] , edades[i])
        break;
    else:
        print("Respuesta incorrecta")