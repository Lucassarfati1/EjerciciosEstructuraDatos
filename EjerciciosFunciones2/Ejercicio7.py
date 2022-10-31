from random import *


def adivinaDado():

    if(n==0):
        n=randint(1,6)
        intento=1
    numUsuario=int(input('Ingrese un numero del dado que cree que salio al tirarlo'))
    if(n==numUsuario):
        print('\n','Acertaste en el intento:',intento)
        return
    else:
        print('No acertaste al numero que salio en el dado, intento nro:',intento)
        intento=intento+1
        adivinaDado()
        

def main():
    
    adivinaDado()
if __name__ == '__main__':
    main()