
def main():
    lista=[25,59,56,47,12,23]
    contador=0
    resultset=0
    for i in lista:
        resultset+=i
        contador+=1
    resultset=resultset/contador
    print('veremos el promedio de los numeros de la lista: ',resultset)
   
if __name__ == '__main__':
    main()