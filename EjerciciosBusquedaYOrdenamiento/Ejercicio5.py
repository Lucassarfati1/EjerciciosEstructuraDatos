#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lucas
#
# Created:     21/11/2022
# Copyright:   (c) lucas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Se cuenta con una lista de canciones de las que se conoce su nombre, nombre de la
#banda o artista, y el año de lanzamiento del álbum.
#a) Realizar un listado ordenado por canción asc
#b) Realizar un listado ordenado por banda o artista asc
#c) Realizar un listado ordenado por año de lanzamiento desc
#d) Determinar si en la lista existe alguna canción de los Guns and Roses;
#e) Mostrar todas las canciones de Nirvana;
#f) Agregar una nueva canción a la lista, y volver a realizar un listado
#ordenado por nombre de canción;
#g) Determinar cuantas canciones de los Red Hot Chili Peppers hay en la lista;
#h) Mostrar toda la información de las canciones "Whisky in the jar".

def main():
    canciones=[
    {'nombre':'War of change','artista o banda:':'Thousand foot krutch','año estreno':'2011'},
    {'nombre':'To the moon','artista o banda:':'Lil cake','año estreno':'2021'},
    {'nombre':'U.S.A','artista o banda:':'Lil cake','año estreno':'2020'},
    {'nombre':'Sweet child O"mine','artista o banda:':'Gun"s roses','año estreno':'2010'},
    {'nombre':'November rain','artista o banda:':'Gun"s roses','año estreno':'2010'},
    {'nombre':'Paradise city','artista o banda:':'Gun"s roses','año estreno':'2010'},
    {'nombre':'The man who sold the world','artista o banda:':'Nirvana','año estreno':'2009'},
    {'nombre':'Comes as you are','artista o banda:':'Nirvana','año estreno':'2009'},
    {'nombre':'In bloom','artista o banda:':'Nirvana','año estreno':'2009'},
    {'nombre':'Where did you sleep last night','artista o banda:':'Nirvana','año estreno':'2020'},
    {'nombre':'Moonlight','artista o banda:':'XXTentacion','año estreno':'2018'},
    {'nombre':'The remedy for a broken heart (why am I so in love)','artista o banda:':'XXTentacion','año estreno':'2018'},
    {'nombre':'Hope','artista o banda:':'XXTentacion','año estreno':'2018'},
    {'nombre':'Californication','artista o banda:':'Red hot chili peppers','año estreno':'2009'},
    {'nombre':'Otherside','artista o banda:':'Red hot chili peppers','año estreno':'2011'},
    {'nombre':'Free speech for the Dumb','artista o banda:':'Metallica','año estreno':'1998'},
    {'nombre':'It"s electric','artista o banda:':'Metallica','año estreno':'1998'},
    {'nombre':'Sabbra cadabra','artista o banda:':'Metallica','año estreno':'1998'},
    {'nombre':'Turn the page','artista o banda:':'Metallica','año estreno':'1998'},
    {'nombre':'Die, die my darling','artista o banda:':'Metallica','año estreno':'1998'},
    {'nombre':'Astronomy','artista o banda:':'Metallica','año estreno':'1998'},
    {'nombre':'Loverman','artista o banda:':'Metallica','año estreno':'1998'},
    {'nombre':'Helpless','artista o banda:':'Metallica','año estreno':'1998'},
    {'nombre':'Blitzkrieg','artista o banda:':'Metallica','año estreno':'1998'},

    ]
    #Ordenamos la lista de canciones en orden alfabetico por canciones
    insercion(canciones)
    print('La lista de canciones es asi:')

    for i in range(0,len(canciones)):
        print(f'Nombre de la cancion:{canciones[i]["nombre"]}, artista o banda: {canciones[i]["artista o banda:"]} , año estreno del album:{canciones[i]["año estreno"]} \n')
    print('Ahora las ordenamos por la banda o artista bro \n')
    #Ordenamos la lista de canciones en orden alfabetico por banda o artista
    burbuja_mejorado(canciones)
    for i in range(0,len(canciones)):
        print(f'Nombre de la cancion:{canciones[i]["nombre"]}, artista o banda: {canciones[i]["artista o banda:"]} , año estreno del album:{canciones[i]["año estreno"]} \n')
    print('Ahora las vamos a ordenar por el año en que se lanzo el album \n')
    seleccion(canciones)
    for i in range(0,len(canciones)):
        print(f'Nombre de la cancion:{canciones[i]["nombre"]}, artista o banda: {canciones[i]["artista o banda:"]} , año estreno del album:{canciones[i]["año estreno"]} \n')
    pos=binaria(canciones,'Gun"s roses')
    #aca mostramos si hay canciones de los gun"s roses en la lista
    if(pos!=-1):
        print('Hay 1 o mas canciones de los Gun"s roses')
    else:
        print('No se encuentran canciones de los Gun"s roses')
    #Mostrar las canciones de nirvana y sus datos
    print('A continuacion mostraremos las canciones de Nirvana que hayan en el array: \n')

    red=0
    metal=[]
    #aca metemos los condicionales para separar las canciones de nirvana, las de mettalica y el contador de las canciones de los red hot chilli peppers
    for i in range(0,len(canciones)):
        if(canciones[i]['artista o banda:']=='Red hot chili peppers'):
            red+=1
        if(canciones[i]['artista o banda:']=='Metallica'):
            metal.append(canciones[i])
        if(canciones[i]['artista o banda:']=='Nirvana'):
            print(f'{canciones[i]}')
    #Agregamos una cancion random a la lista
    canciones.append({'nombre':'Session #50','artista o banda:':'Duki ft Bizzarrap','Año estreno':'2022'})
    #Volvemos a ordenar la lista por cancion asc
    insercion(canciones)
    #Aca imprimimos cuantas canciones de los red hot chili peppers hay en la lista
    print(f'\n En el array hay {red} canciones de los red hot chili peppers')
    #Aca mostramos toda la informacion que hay de las canciones que estuvieron en el album wisky in the jar
    print('Aca esta toda la informacion de todas las canciones que tiene el array del album "wisky in the jar"')
    for i in range(0,len(metal)):
        print(metal[i])

    pass
def binaria(lista, buscado) :
    """ Metodo de busqueda binaria """
    posicion = -1
    primero = 0
    ultimo = len(lista) - 1
    while (primero <= ultimo) and (posicion == -1) :
        medio = (primero + ultimo) // 2
        if (lista[medio]['artista o banda:'] == buscado) :
            posicion = medio
        else :
            if (buscado < lista[medio]['artista o banda:']) :
                ultimo = medio - 1
            else :
                primero = medio + 1
    return posicion
def insercion(lista) :
    """Método de ordenamiento inserción"""
    for i in range(1, len(lista)+1) :
        k = i-1
        while (k > 0) and (lista[k]['nombre'] < lista[k-1]['nombre']) :
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k -= 1
def burbuja_mejorado(lista) :
    """Método de ordenamiento burbuja mejorado"""
    i = 0
    control = True
    while (i <= len(lista)-2) and control :
        control = False
        for j in range(0, len(lista)-i-1) :
            if (lista[j]['artista o banda:'] > lista[j+1]['artista o banda:']) :
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control = True
        i += 1
def seleccion(lista) :
    """Método de ordenamiento selección"""
    for i in range(0, len(lista)-1) :
        minimo = i
        for j in range(i+1, len(lista)) :
            if (lista[j]['año estreno'] > lista[minimo]['año estreno']) :
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]
if __name__ == '__main__':
    main()
