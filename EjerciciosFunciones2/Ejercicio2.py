def ejercicio2():
    libreria=[]
    ingresarDatos(libreria)
    
    cantidadTotalLibros=0
    precioTotal=0
    for libro in libreria:

        print('Nro ISBN:', libro['ISBN'],'\n')
        print('Nombre del libro:', libro['Nombre del libro'],'\n')
        print('Stock libro: ', libro['Stock del libro'],'\n')
        print('Precio del libro:', libro['Precio del libro'],'\n')

        precioTotalDelLibro=libro['Stock del libro']*libro['Precio del libro']

        cantidadTotalLibros+=libro['Stock del libro']

        precioTotal+=precioTotalDelLibro

        
        
    print('\n La cantidad de libros total:',cantidadTotalLibros)
    print('\n El monto total de Libros es de:',precioTotal)
    print('\n El valor promedio de los libros es:',precioTotal/cantidadTotalLibros)



def ingresarDatos(libreria):
    libro={}
    ISBN=input('Ingrese el isbn codigo del libro:')
    if(int(ISBN) == 0):
        return
    
    
    nombreLibro=input('Ingrese el nombre del libro')
    stockLibro=int(input('Ingrese el stock del libro'))
    precioLibro=int(input('Ingrese el precio del libro'))

    

    libro={
    'ISBN': ISBN,
    'Nombre del libro': nombreLibro,
    'Stock del libro':stockLibro,
    'Precio del libro':precioLibro
    }
    libreria.append(libro)
    ingresarDatos(libreria)

def main():
    ejercicio2()
if __name__ == '__main__':
    main()