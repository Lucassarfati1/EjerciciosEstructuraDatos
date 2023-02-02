#-------------------------------------------------------------------------------
# Name:        Ejercicio3
# Purpose:
#
# Author:      lucas
#
# Created:     21/11/2022
# Copyright:   (c) lucas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Dada una lista de personajes de la saga de Star Wars de las que se conoce su nombre,
#resolver la siguientes tareas:
#a) Listar los personajes ordenados alfabéticamente de manera ascendente
#b) Determinar si el personaje "Darth Maul" está cargado y en qué posición se
#encuentra;
#c) Mostrar la información de los personajes que se encuentran antes y después
#de "Hera Syndulla";
#d) Listar todos los personajes que comienzan con la letra L;
#Note: Los algoritmos de ordenamiento que se vieron en clase, sirven tanto para
#listas de enteros como para listas de cadenas de texto.

def main():
    #Creamos la lista de los pjs de star wars
    pjs=['Darth Vader','Luke Skywalker','Leia organa','Darth Maul','Han solo','Yoda','Obi-Wan Kenobi','Kylo Ren','R2-D2','Palpatine','Hera Syndulla','Dooku','Ben Skywalker','Chewbacca']
    #Ordenamos la lista alfabeticamente con un sort burbuja
    burbuja(pjs)
    #Imprimimos los resultados con un ciclo for
    #Buscamos la posicion del personaje "Darth Maul"
    pos=secuencial(pjs,'Darth Maul')
    for i in range(0,len(pjs)):
        print(f'Personaje: {pjs[i]} ')
    l=[]

    if(pos!=-1):
            print(f'El personaje {pjs[pos]} esta cargado y se encuentra en la posicion {pos}')
    else:
        print('El personaje Darth Maul no ha sido encontrado')

    for i in range(0,len(pjs)):
        #Preguntamos si el personaje empieza con  la letra L
        if(pjs[i].startswith('l')or pjs[i].startswith('L')):
            l.append(pjs[i])
        #Imprimimos los personajes que hay antes y despues de Hera Syndulla
        if(pjs[i]=='Hera Syndulla'):
            print('Los personajes que hay antes de Hera syndulla son: \n')
            for t in range(0,i-1):
                print(f'{pjs[t]}')
            print('Los personajes que hay despues de Hera Syndulla son: \n')
            for j in range (i+1,len(pjs)):
                print(f'{pjs[j]}')
    #Imprimimos todos los personajes de star wars que arrancan con la letra L
    print(f'Todos los personajes de star wars que empiezan con la letra L son: \n')
    print(l)
#Definios los metodos que vamos a necesitar en el programa, uno de ordenamiento y el otro de busqueda
def burbuja(lista) :
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j][0] > lista[j+1][0]) :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    pass
def secuencial(lista, buscado) :
    """ Metodo de busqueda secuencial """
    posicion = -1

    for i in range(0, len(lista)) :
        if (lista[i]==buscado) :
            posicion = i

    return posicion
if __name__ == '__main__':
    main()
