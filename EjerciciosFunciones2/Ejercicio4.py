def mostrarValores(victor,indice):
    if(indice<0):
        return 0
    else:
        print(victor[indice])
        return mostrarValores(victor,indice-1)
def main():
    mostrarValores([3,92,38,39,39],len([3,92,38,39,39])-1)
if __name__ == '__main__':
    main()