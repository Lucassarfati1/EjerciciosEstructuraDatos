#-------------------------------------------------------------------------------
# Name:        Ejercicio 4
# Purpose:
#
# Author:      lucas
#
# Created:     22/11/2022
# Copyright:   (c) lucas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Determinar si una cadena de caracteres es un palíndromo.

def main():
    palabra=input('Introduce una palabra para saber si es polindromo')
    miPila=Pila()
    miOtraPila=Pila()
    for i in range(0,len(palabra)-1):
        miPila.apilar(palabra[i])
    for i in range(0,len(palabra)-1):
        datovich=miPila.desapilar()
        miOtraPila.apilar(datovich)
    for i in range(0,len(palabra)-1):
        miPila.apilar(palabra[i])
    if(miOtraPila==miPila):
        print(f'La palabra {palabra} es polindromo')
    else:
        print(f'La palabra {palabra} no es polindromo')

    pass
class nodoPila(object) :
    """Clase nodo pila"""
    info, sig = None, None

class Pila(object) :
    """Clase Pila"""
    def __init__(self) :
        self.cima = None
        self.tamanio = 0

    def apilar(self, dato) :
        """Apila el elemento sobre la cima de la pila"""
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = self.cima

        self.cima = nodo
        self.tamanio += 1

    def desapilar(self) :
        """Desapila el elemento de la cima de la pila y lo devuelve"""
        x = self.cima.info
        self.cima = self.cima.sig
        self.tamanio -= 1

        return x

    def pila_vacia(self) :
        """Devuelve true si la pila está vacía"""
        return self.cima is None

    def en_cima(self) :
        """Devuelve el valor almacenado en la cima de la pila"""
        if self.cima is not None :
            return self.cima.info
        else :
            return None

    def tamanio(self) :
        """Devuelve el nro de elementos en la pila"""
        return self.tamanio
if __name__ == '__main__':
    main()
