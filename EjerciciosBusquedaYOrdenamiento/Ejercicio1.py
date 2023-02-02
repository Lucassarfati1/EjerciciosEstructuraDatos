
# 1) Para probar los distintos algoritmos de ordenamiento vistos (Burbuja, Selección,
# Inserción, Rápido y Mezcla):
# a) Generar una lista de elementos aleatorios de distintos tamaños (100.000,1.000.000, 10.000.000)
# b) Medir y mostrar su tiempo de ejecución
# c) Medir y mostrar la cantidad de comparaciones realizadas
# d) Deberá indicar nombre y tiempo del método más rápido
# e) Deberá indicar nombre y cantidad del método que realiza menos comparaciones

import time
import random
def main():

    listaCien=[]
    listaMil=[]
    listaDiezMil=[]


    ahora=time.time()

    for i in range(0,100):


        listaCien.append(random.randint(0, 100))

        finalCienMil=ahora-time.time()

    print(f'La cantidad de elementos de nuestro array es de: {len(listaCien)}')

    print(f'El tiempo que tardo python en cargar los cien numeros randoms es: {finalCienMil}s')



    ahora=time.time()



    for i in range(0,1000):

        listaMil.append(random.randint(0, 100))



    finalMillon=ahora-time.time()

    print('La cantidad de elementos de nuestro array es de: ',len(listaMil))

    print('El tiempo que tardo python en cargar  mil de numeros randoms es:',finalMillon,'s')



    ahora=time.time()

    for i in range(0,10000):

        listaDiezMil.append(random.randint(0, 100))

    finalDiezMillones=ahora-time.time()

    print('La cantidad de elementos de nuestro array es de: ',len(listaDiezMil))

    print('El tiempo que tardo python en cargar diez mil de numeros randoms es:',finalDiezMillones,'s')

    ahora=time.time()
    contador=0
    burbuja(listaCien)
    print('Termina la funcion burbuja para lista de cien elementos')
    finalBurbuja=ahora-time.time()

    print(f'El metodo burbuja tarda {finalBurbuja} para ordenar los cien elementos de numeros')

    ahora=time.time()
    contador=0
    burbuja(listaMil)
    print('Termina la funcion burbuja para lista de mil elementos')
    finalBurbuja=ahora-time.time()

    print(f'El metodo burbuja tarda {finalBurbuja} para ordenar los mil elementos de numeros')
    ahora=time.time()
    contador=0
    #burbuja(listaDiezMil)
    #print('Termina la funcion burbuja')
    #finalBurbuja=ahora-time.time()

    #print(f'El metodo burbuja tarda {finalBurbuja} para ordenar los Diez Mil elementos de numeros')


    seleccion(listaCien)
    print('Termina la funcion seleccion para lista de cien elementos')
    finalBurbuja=ahora-time.time()

    print(f'El metodo seleccion tarda {finalBurbuja} para ordenar los cien elementos de numeros')

    contador=0
    seleccion(listaMil)
    print('Termina la funcion seleccion para lista de mil elementos')
    finalBurbuja=ahora-time.time()

    print(f'El metodo seleccion tarda {finalBurbuja} para ordenar los mil elementos de numeros')

    contador=0
    insercion(listaCien)
    print('Termina la funcion insercion para lista de cien elementos')
    finalBurbuja=ahora-time.time()

    print(f'El metodo de insercion tarda {finalBurbuja} para ordenar los cien elementos de numeros')

    contador=0
    insercion(listaMil)
    print('Termina la funcion insercion para lista de mil elementos')
    finalBurbuja=ahora-time.time()

    print(f'El metodo de insercion tarda {finalBurbuja} para ordenar los mil elementos de numeros')



#Metodo de ordenamiento burbuja
def burbuja(listovich) :
    contador=0
    for i in range(0, len(listovich)-1) :
        if(i==len(listovich)-2):
            print(f'El metodo burbuja realiza {contador+1} tantas comparaciones para ordenar los numeros de la lista  \n')
        for j in range(0, len(listovich)-i-1) :

            if (listovich[j] > listovich[j+1]) :

                listovich[j], listovich[j+1] = listovich[j+1], listovich[j]


                contador=contador+1
def quicksort(lista, primero, ultimo) :
 """Metodo de ordenamiento quicksort"""
 izquierda = primero
 derecha = ultimo - 1
 pivote = ultimo

 while (izquierda < derecha) :
    while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha) :
        contador=contador+1
        izquierda += 1

    while (lista[derecha] > lista[pivote]) and (derecha >= izquierda) :
        contador=contador+1
        derecha -= 1

    if (izquierda < derecha) :
                contador=contador+1
                lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

 if (lista[pivote] < lista[izquierda]) :
    contador=contador+1
    lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]

 if (primero < izquierda) :
    contador=contador+1
    quicksort(lista, primero, izquierda-1)

 if (ultimo > izquierda) :
    contador=contador+1
    quicksort(lista, izquierda+1, ultimo)

def mergesort(lista) :
 """Metodo de ordenamiento mergesort"""

 if (len(lista) <= 1) :
    return lista
 else :
    medio = len(lista) // 2
    izquierda = []

    for i in range(0, medio) :
        izquierda.append(lista[i])

    derecha = []

    for i in range(medio, len(lista)) :
        derecha.append(lista[i])

    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)

    if (izquierda[medio-1] <= derecha[0]) :
        izquierda += derecha

        return izquierda

    resultado = merge(izquierda, derecha)

    return resultado

def insercion(lista) :
 """Método de ordenamiento inserción"""
 contador=0
 for i in range(1, len(lista)+1) :
    if(i==len(lista)):
        print(f'El metodo de insercion realiza {contador+1} tantas comparaciones para ordenar los numeros de la lista \n')
    k = i-1
    while (k > 0) and (lista[k] < lista[k-1]) :
        contador=contador+1
        lista[k], lista[k-1] = lista[k-1], lista[k]
        k -= 1

def seleccion(lista):
    contador=0
 #"""Método de ordenamiento selección"""
    for i in range(0, len(lista)-1):
        contador=contador+1
        if(i==len(lista)-2):
            print(f'El metodo de seleccion realiza {contador+1} tantas comparaciones para ordenar los numeros de la lista \n')
        minimo = i
        for j in range(i+1, len(lista)) :
            if (lista[j] < lista[minimo]) :
                minimo = j
                contador=contador+1

        lista[i], lista[minimo] = lista[minimo], lista[i]
if __name__ == '__main__':
    main()