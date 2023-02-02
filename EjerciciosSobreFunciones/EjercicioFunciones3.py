def relacion():
    num1=int(input('introduce el primer numero'))
    num2=int(input('introduce el segundo numero'))
    if(num1>num2):
        return 1
    elif(num1==num2):
        return 0
    else:
        return -1
def main():
    resultset=relacion()
    print('Si el primer numero es mayor que el segundo retorna 1, sino retorna -1, y si son iguales retorna 0. Resultado: ',resultset)
if __name__ == '__main__':
    main()