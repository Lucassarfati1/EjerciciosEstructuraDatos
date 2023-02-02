#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      lucas
#
# Created:     22/11/2022
# Copyright:   (c) lucas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como
#estructura extra.
def main():


    #Creamos el array de elementos y el de ocurrencias de cada elemento
    elementos=[2,3,3,1,2,3,4,4,5,4,5,4,3,4,4,2,5,6,7,7,8]
    miPila=Pila()

#Apilamos los elementos
    for i in range(0,len(elementos)):

        miPila.apilar(elementos[i])
        #def invertir(self):
    otraPila=Pila()

    while(not miPila.pila_vacia()):
        datovicho=miPila.desapilar()
        otraPila.apilar(datovicho)
    miPila=otraPila

    while(not miPila.pila_vacia()):
        datovich=miPila.desapilar()
        print(f'{datovich}')


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
