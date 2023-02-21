#Creamos dos variables donde vamos a almencenar el número de libras o kilogramos que nos den.
libras = 0.0
kilos = 0.0

#Generamos un input donde diremos al usuario que palabra clave debe usar para acceder a las funciones del programa y registramos la respuesta en una variable
respuesta = input("Si quieres converir de kilos a libras pulsa 'k',si quieres convertir de libras a kilos pulsa 'l' ")

#Realizamos una serie de if para validar la resouesta del usuario
#Si el usuario respode k o K lo que haremos sera preguntar cuantos kilogramos desea convertir a libras
if(respuesta == "k" or respuesta == "K"):
    print("Conversor de Kilogramos a Libras")
    kilos = float(input("Introduce la cantidad de kilos "))#Convertimos la respuesta a numero decimal para que se trate como un numero y no texto
    kilosC = round(kilos*2.2, 2)#Aplicamos una formula para convertir los kilogramos en libras
    print(f"{kilos} kilogramos son {kilosC} libras ")#Mostramos la respuesta por pantalla
#Si el usuario respode l o L lo que haremos sera preguntar cuantas libras desea convertir a kilogramos
elif(respuesta == "l" or respuesta == "L"):
    print("Conversor de Libras a Kilogramos")
    libras = float(input("Introduce la cantidad de libras "))
    librasC = round(libras*0.453, 3)#Aplicamos una formula para convertir las libras en kilogramos
    print(f"{libras} libras son {librasC} kilogramos ")#Mostramos la respuesta por pantalla
else:
    print("La respuesta no es valida")#En caso de no dar una respuesta valida(k,K,l,L), se le dira al usuario que su respuesta no ha sido valida
