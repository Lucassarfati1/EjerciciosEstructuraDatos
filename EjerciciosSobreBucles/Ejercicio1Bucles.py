#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lucas
#
# Created:     03/10/2022
# Copyright:   (c) lucas 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    var=int(input('ingrese un numero impar'))
    while(var%2==0):
        var=int(input('ingrese un numero IMPAR, no PAR.'))

    print('Felicidades, pudiste ingresar un numero impar')
if __name__ == '__main__':
    main()
