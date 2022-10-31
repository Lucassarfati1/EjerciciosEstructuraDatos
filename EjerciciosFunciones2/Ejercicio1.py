def ejercicio1():
    lista=[]
    promedioSuc=0
    totalVendido=0
    nomSuc=input('Ingrese el nombre de la sucursal')
    cantVentas=input('Ingrese la cantidad de ventas')
    ventaSuc=input('Ingrese la venta total de la sucursal')
    lista.append(nomSuc)
    lista.append(cantVentas)
    lista.append(ventaSuc)
    promedioSuc=ventaSuc/cantVentas

    if(nomSuc==0):
        print('Sucursal:',nomSuc)
        print('Cantidad de ventas',cantVentas)
        print('Cantidad de ventas de la sucursal',cantVentas)
        print('Promedio de cada sucursal:',cantVentas)
def main():
    ejercicio1()
if __name__ == '__main__':
    main()