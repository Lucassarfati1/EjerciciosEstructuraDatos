#Ejercicio 1
nombre=input('Como es su nombre de usuario')
lineas=int(input('Introduce cuantas lineas quiere'))
print((f'{nombre}\n')*lineas)
#Ejercicio 2
nombre=input('Como es su nombre completo de usuario')
print(f'Nombre completo de usuario:\n -{nombre.lower()} \n -{nombre.upper()} \n -{nombre.capitalize()}')
#Ejercicio 3
nombre=input('Como es su nombre completo de usuario')
numLetras=len(nombre)
print(f'{nombre.upper()} tiene {numLetras} letras')
#Ejercicio 4
numero=input('Ingrese su numero con prefijo y codigo de area')
print(f'Su numero sin prefijo ni codigo de area es: {numero[7:]}')
#Ejercicio 5
frase=input('Introduce una frase')
print(f'La frase invertida es asi {frase[::-1]}')
#Ejercicio 6
frase=input('Introduce una frase')
vocal=input('Introduce una vocal')
print(f'{frase.replace(vocal,vocal.upper())}')
#Ejercicio 7
email=input('Ingrese un mail')
print(email[:email.find('@')] + '@edu.ar')
#Ejercicio 8
precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'pesos y', precio[precio.find('.')+1:], 'centavos.')

#Ejercicio 9
fecha = input("Introduce la fecha de nacimiento dd/mm/aaaa: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])
fecha = input("Introduce la fecha de nacimiento en formato día/mes/anio: ")
dia = fecha[:fecha.find('/')]
mesanio = fecha[fecha.find('/')+1:]
mes = mesanio[:mesanio.find('/')]
anio = mesanio[mesanio.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('anio', anio)

#Ejercicio 10
canasta = input('Introduce los productos del canasto de la compra separados por comas: ')
print(canasta.replace(',', '\n'))

#Ejercicio 11
producto=input('Introduce el nombre del producto')
precio=float(input('Introduce el precio del producto'))
cantidad=int(input('Introduce la cantidad del pedido'))
total=precio*cantidad
print(f'{producto}: {precio:6.2f} X {cantidad:3} = {total:8.2f}')