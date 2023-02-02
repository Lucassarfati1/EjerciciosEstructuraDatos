def main():
    num1=int(input('Ingrese el primer numero'))
    num2=int(input('Ingrese el segundo numero'))
    operacion=int(input('Ingrese el numero dependiendo de la operacion que quiera hacer 1.Sumar/2.Restar/3.Multiplicar'))

    while(not(operacion==1 or operacion==2 or operacion==3)):
        operacion=int(input('Ingrese bien la operacion sino no podremos continuar,1.Sumar/2.Restar/3.Multiplicar'))

    resultset=0
    if(operacion==1):
        resultset=num1+num2
    elif(operacion==2):
        resultset=num1-num2
    elif(operacion==3):
        resultset=num1*num2
    print(f'El resultado de la operacion es',resultset)

if __name__ == '__main__':
    main()