def separar(lista):
    
    pares=[]
    impares=[]
    for i in lista:
        if(i % 2==0):
            pares.append(i)
        else:
            impares.append(i)
        
    return pares,impares
    
    
def main():
    listovich=[23,42,55,92,77,54]
    pares,impares=separar(listovich)
    print('numeros pares:',pares)
    print('numeros impares:',impares)
    
if __name__ == '__main__':
    main()