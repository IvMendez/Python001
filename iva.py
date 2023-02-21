#Mostramos un titulo que indica la funcion que hara nuestro programa
print("Calculadora de IVA")
#Aplicamos un input donde le preguntamos al usuario si quiere sumar o restar el iva
decision = input("Desea 'sumar' o 'restar' IVA ")
#Hacemos un if-elif-else para validar la respuesta del usuario y hacer en base a su decision
if decision=="sumar" or decision=="SUMAR":
    precio = float(input("Indica el precio del producto "))#Si el usuario decide sumar le pedimos el precio del producto y validamos que no de un numero negativo o 0
    if precio >0:
        iva = float(input("Indica el IVA a aplicar "))#Hacemos los mismo con el iva para validarlo
        if iva >0:
         precio_con_iva= round(precio+(precio*(iva/100)), 2)#Aplicamos la formula para sacar el calculo del precio con el iva
         print(f"Precio sin iva = {precio}")#Mostramos el resultado por pantalla
         print("")
         print(f"IVA = {iva}")
         print("")
         print(f"Precio con IVA = {precio_con_iva}")
        else:
         print("IVA incorrecto")
    else:
         print("Precio incorrecto")
elif decision=="restar" or decision=="RESTAR":
    precio = float(input("Indica el precio del producto "))#Si el usuario decide restar le pedimos el precio del producto y validamos que no de un numero negativo o 0
    if precio >0:
        iva = float(input("Indica el IVA aplicado "))#Hacemos los mismo con el iva para validarlo
        if iva >0:
         precio_sin_iva=round(precio-precio*(iva/100), 2)#Aplicamos la formula para sacar el calculo del precio con el iva
         print(f"Precio con iva = {precio}")#Mostramos el resultado por pantalla
         print("")
         print(f"IVA = {iva}")
         print("")
         print(f"Precio sin IVA = {precio_sin_iva}")
        else:
         print("IVA incorrecto")
    else:
         print("Precio incorrecto")
else:
    print("Respuesta erronea indique si quiere 'sumar' o 'restar'")#Si no ha indicado una decision valida se lo indicamos al usuario
