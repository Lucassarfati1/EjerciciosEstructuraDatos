def libross():
    libreria=[{}]
    ISBN=input('Ingrese el isbn codigo del libro:')
    nombreLibro=input('Ingrese el nombre del libro')
    stockLibro=input('Ingrese el stock del libro')
    precioLibro=input('Ingrese el precio del libro')
    libreria=[{'ISBN':ISBN,'Nombre del libro':nombreLibro,'Stock del libro':stockLibro,'Precio del libro':precioLibro}]
    if(ISBN==0):
        print('ISBN:',ISBN)
        print('Nombre del libro',nombreLibro)
        print('Stock del libro',stockLibro)
        print('Precio del libro:',precioLibro)


def main():
    libross()
if __name__ == '__main__':
    main()