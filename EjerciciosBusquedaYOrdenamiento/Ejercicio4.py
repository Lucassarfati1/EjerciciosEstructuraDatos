#-------------------------------------------------------------------------------
# Name:        Ejercicio 4
# Purpose:
#
# Author:      lucas
#
# Created:     21/11/2022
# Copyright:   (c) lucas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Se dispone de una lista de películas con la siguiente información: título, año de
#estreno, recaudación y valoración del público (de 1 a 5), los cuales debemos procesar
#contemplando las siguiente tareas:
#a) Realizar un listado ordenado por título de manera ascendente
#b) Realizar un listado ordenado por año de lanzamiento de manera ascendente
#c) Realizar un listado ordenado por recaudación de manera descendente;
#d) Mostrar toda la información de la película que más recaudo;
#e) Listar todas las películas que tenga valoración 5;
#f) Determinar si la película “Avengers: Infinity War” está en la lista y
#mostrar toda su información;
#g) Indicar en qué posición se encuentra la película “Star Wars: The Return of
#Jedi”;
#h) Calcular el total recaudado por las películas que en su título incluyen la
#palabra “Avengers”;
#i) Mostrar todas las películas que se estrenaron en el año 2017;
#j) Listar todas las películas que comienzan con la palabra “Iron”.
def main():
    pelis=[
    {'titulo':'El ocaso del samurai','Año Estreno':'2002','Recaudacion':10000,'Opinion':5},
    {'titulo':'La espada del samurai','Año Estreno':'2003','Recaudacion':12000,'Opinion':4},
    {'titulo':'Azumi','Año Estreno':'2003','Recaudacion':10000,'Opinion':2},
    {'titulo':'Avengers: Infinity War','Año Estreno':'2015','Recaudacion':35000,'Opinion':5},
    {'titulo':'Zatoichi','Año Estreno':'2003','Recaudacion':80000,'Opinion':3},
    {'titulo':'Hana','Año Estreno':'2006','Recaudacion':11000,'Opinion':2},
    {'titulo':'Star Wars: The Return of Jedi','Año Estreno':'2005','Recaudacion':28000,'Opinion':5},
    {'titulo':'Scabbard samurai','Año Estreno':'2010','Recaudacion':20000,'Opinion':3},
    {'titulo':'Avengers: La trolita barata','Año Estreno':'2018','Recaudacion':42000,'Opinion':4},
    {'titulo':'13 Asesinos','Año Estreno':'2010','Recaudacion':13000,'Opinion':3},
    {'titulo':'Sword of desesperation','Año Estreno':'2010','Recaudacion':15000,'Opinion':5},
    {'titulo':'Hara-Kiri:Muerte de un samurai','Año Estreno':'2011','Recaudacion':25000,'Opinion':4},
    {'titulo':'Kenshin, el guerrero samurai','Año Estreno':'2012','Recaudacion':17000,'Opinion':4},
    {'titulo':'La espada del inmortal','Año Estreno':'2017','Recaudacion':11500,'Opinion':3},
    {'titulo':'Avengers: El regreso de los boluditos','Año Estreno':'2017','Recaudacion':52000,'Opinion':5},
    {'titulo':'Narutovich','Año Estreno':'2012','Recaudacion':1000000,'Opinion':5}
    ]
    #Ordenamos alfabeticamente las peliculas
    burbuja(pelis)
    #Imprimimos las peliculas
    for i in range(0,len(pelis)):
        print(pelis[i])
    print('\n')
    print('\n')
    print('\n')
    #Ordenamos las pelis de forma ascendente dependiendo del año de estreno e imprimimos
    insercion(pelis)
    for i in range(0,len(pelis)):
        print(pelis[i])
    print('\n')
    print('\n')
    print('\n')
    #Ordenamos las pelis de forma ascendente dependiendo de la recaudacion, revertimos la lista para que quede ascendente e imprimimos
    #tambien creamos un array para guardar las pelis mas aclamadas por el publico y un diccionario de una pelicula para despues preguntarle al programa si existe esa pelicula en el array de pelis
    quicksort(pelis,0,len(pelis)-1)
    pelis.reverse()
    top=[]
    pelis2017=[]
    avenger=[]
    iron=[]
    avengers={
    'existencia':False,
    'pos': 0
    }

    for i in range(0,len(pelis)):
        if(pelis[i]['titulo'].startswith('Iron')):
            iron.append(pelis[i])
        if(pelis[i]['Año Estreno']=='2017'):
            pelis2017.append(pelis[i])
        if(pelis[i]['titulo'].find('Avengers')!=-1):
            avenger.append(pelis[i])
        if(pelis[i]['titulo']=='Avengers: Infinity War'):
            avengers['existencia']='True'
            avengers['pos']=i

        if(pelis[i]['Opinion']>4):
            top.append(pelis[i])
        print(pelis[i])
    #Imprimimos los datos de la peli que mas recaudo
    print(f'\n Estos son los datos de la pelicula que mas recaudo: {pelis[0]}')
    #Imprimimos los datos de las pelis mas aclamadas por el publico
    print(f'\n Las peliculas mas aclamadas por el publico son: {top} \n')
    #Imprimimos los datos de la peli avengers si existe
    if(avengers['existencia']):
        print(pelis[avengers['pos']])
    posgre=centinela(pelis,'Star Wars: The Return of Jedi')
    if(posgre!=-1):
        print(f'\n La pelicula Star Wars: The Return of Jedi esta en el indice {posgre}')
    else:
        print('\n La pelicula star wars: the return of jedi no se ha encontrado')
    centinela(pelis,'Avengers')
    total=0
    for i in range(0,len(avenger)):
        total+=avenger[i]['Recaudacion']
    print(f'El total recaudado por las peliculas de los Avengers es: {total}')

    print(f'\n Las peliculas que se estrenaron en el año 2017 fueron: {pelis2017}')

    print(f'Aca esta el listado de peliculas que empiezan con la palabra "Iron": ')
    pass
def burbuja(lista) :
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j]['titulo'] > lista[j+1]['titulo']) :
                lista[j], lista[j+1] = lista[j+1], lista[j]
def insercion(lista) :
    """Método de ordenamiento inserción"""
    for i in range(1, len(lista)+1) :
        k = i-1
        while (k > 0) and (lista[k]['Año Estreno'] < lista[k-1]['Año Estreno']) :
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k -= 1

def quicksort(lista, primero, ultimo) :
    """Metodo de ordenamiento quicksort"""
    izquierda = primero
    derecha = ultimo - 1
    pivote = ultimo

    while (izquierda < derecha) :
        while (lista[izquierda]['Recaudacion'] < lista[pivote]['Recaudacion']) and (izquierda <= derecha) :
            izquierda += 1

        while (lista[derecha]['Recaudacion'] > lista[pivote]['Recaudacion']) and (derecha >= izquierda) :
            derecha -= 1

        if (izquierda < derecha) :
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

    if (lista[pivote]['Recaudacion'] < lista[izquierda]['Recaudacion']) :
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]

    if (primero < izquierda) :
        quicksort(lista, primero, izquierda-1)

    if (ultimo > izquierda) :
        quicksort(lista, izquierda+1, ultimo)
def centinela(lista, buscado) :
    """ Metodo de busqueda secuencial con centinela """
    posicion = -1
    i = 0
    while (i < len(lista)) and (posicion == -1) :
        if (lista[i]['titulo'] == buscado) :
            posicion = i

        i += 1
    return posicion

if __name__ == '__main__':
    main()
