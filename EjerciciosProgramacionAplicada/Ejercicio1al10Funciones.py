#Ejercicio 1
def saludoGeneral():
    print('¡Hola Amigos!')
#Ejercicio 2
def saludoConNombre(nombre):
    print('¡Hola ' + nombre +'!')
    return

#Ejercicio 3
def factorial(numero):
    numerovich = 1
    for i in range(numero):
        numerovich *= i+1
    return numerovich
#Ejercicio 4
def invoice(precio, iva=21):

    return precio + precio*iva/100
#Ejercicio 5
def areaCirculo(radio):
    numpi = 3.1415
    return numpi*radio**2

def cilinder_volume(radio, altura):

    return areaCirculo(radio)*altura
#Ejercicio 6
def promedio(numeros):
    return sum(numeros)/len(numeros)
#Ejercicio 7

#Ejercicio 8

#Ejercicio 9

#Ejercicio 10

#Ejercicio 11