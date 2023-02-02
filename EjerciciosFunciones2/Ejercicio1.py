# Ejercicio 1.
# Se deberá sacar el promedio de ventas en pesos de esa sucursal

def ejercicio1() :
    # Genere una lista vacía que luego se irá llenando según lo que ingrese el usuario.
    datos = []

    ingresarDatos(datos)

    # Cuando el usuario ingrese un 0 como nombre de sucursal se deberá imprimir:
    # - Todos los datos ingresados
    # - El promedio de cada sucursal
    # - El total vendido por toda la cadena
    for dato in datos :
        print('Nro Sucursal: ', dato[0])
        print('Nombre: ', dato[1])
        print('Cantidad de ventas: ', dato[2])
        print('Total ventas: ', dato[3])
        print('Venta promedio:', dato[4], '\n')

# Pedir los siguientes datos:
# - Nro de sucursal
# - Nombre de sucursal
# - Cantidad de ventas
# - Venta total de la sucursal
def ingresarDatos(datos) :
    lista = []
    nroSuc = input('Ingrese el nro de la sucursal: ')

    if (int(nroSuc) == 0) :
        return

    nomSuc = input('Ingrese el nombre de la sucursal: ')
    cantVtas = input('Ingrese la cantidad de ventas: ')
    ventaSuc = input('Ingrese la venta total de la sucursal:')
    promedioSuc = int(ventaSuc) / int(cantVtas)

    lista.append(nroSuc)
    lista.append(nomSuc)
    lista.append(cantVtas)
    lista.append(ventaSuc)
    lista.append(promedioSuc)

    datos.append(lista)

    ingresarDatos(datos)

def main():
    ejercicio1()
if __name__ == '__main__':
    main()