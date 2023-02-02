def mostrarValores(victor,indice):
    if(indice>len(victor)-1):
        return 0
    else:
        print(victor[indice])
        mostrarValores(victor,indice+1)

def main():
    mostrarValores([3,92,38,39,39],0)
if __name__ == '__main__':
    main()