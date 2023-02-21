#Reto 3

#Crear un juego para adivinar la edad de un usuario

print("Voy a adivinar tu edad, piensa en ella")
while True:
    multi = input("Coge tu edad y multiplicalos por 2 , cuando estes listo pon s ")#Le decimos al usuario que relice una serie de operaciones con su edad
    if multi=="s" or multi=="S":
        suma = input("Sumale 4 al resultado, cuando estes listo pon s ")
        if suma=="s" or suma=="S":
            division = input("Dividelo entre 2, cuando estes listo pon s ")
            if division=="s" or division=="S":
                resultado = float(input("Pon aqui el resultado de las operaciones: "))#Le pedimos que nos de el resultado que le da tras realizar las operaciones
                resultado = ((resultado*2)-4)/2#Inverimos las operaciones para que nos de su edad
                respuesta = input(f"Tu edad es {resultado}? , (s/n)")
                if respuesta=="s" or respuesta=="S":#Si es la adecuada se lo comunicamos
                    print("Ja!!, lo adivine")
                    break
                elif respuesta=="n" or respuesta=="N":#Si no le indicamos que se ha confundido y que lo vuelva a intentar
                    print("Creo que te has equivocado en los calculos,intentalo de nuevo")
                else:
                    print("Respuesta inocorrecta")
            else:
                print("Respuesta inocorrecta")
        else:
            print("Respuesta inocorrecta")
    else:
        print("Respuesta inocorrecta")



