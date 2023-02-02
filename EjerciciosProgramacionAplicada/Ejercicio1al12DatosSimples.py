#Ejercicio 1
print('Hola, estamos aprendiendo python!.')
#Ejercicio 2
variable='Hola, estamos aprendiendo python!.'

print(variable)
#Ejercicio 3
nomUser=input('Ingresa nombre y apellido del usuario')

print(f'¡Hola {nomUser}!')

#Ejercicio 4
print('El resultado es:',(345+2229)*2)

#Ejercicio 5
hsTrabajo=int(input('Ingrese las horas trabajadas'))

hsValor=int(input('Ingrese cuanto cobra por hora'))

print('Al usuario le corresponde:',hsTrabajo*hsValor,'$')

#Ejercicio 6
num=int(input('Introduce el numero'))
resul=0
for i in range(1,num):
    resul+=i
resul+=num
print(f'El resultado es:{resul}')
#Ejercicio 7
peso=float(input('Introduce el peso en kg'))
altura=float(input('Introduce la estatura en METROS'))
indiceMasaCorporal=peso/(altura*altura)
print(f'Tu índice de masa corporal es {indiceMasaCorporal:.2f}')

#Ejercicio 8
dividendo=int(input('Introduce el dividendo'))
divisor=int(input('Introduce el divisor'))
cociente=dividendo/divisor
resto=dividendo%divisor
print(f'La {dividendo} entre {divisor} da un cociente {cociente} y un resto {resto}')

#Ejercicio 9
plataInvertida=int(input('Ingrese la plata que quiere invertir'))
intereses=float(input('Que % de interes anual tiene su inversion?'))
anios=int(input('Cuantos años va a dejar la inversion'))
resultadoAnual=0
resultadoTotal=0
for i in range(0,anios):
    resultadoAnual=plataInvertida*(intereses/100)
    plataInvertida+=resultadoAnual
print(f'El capital obtenido por la inversion es: {plataInvertida}')

#Ejercicio 10
pesoPayaso=112
pesoMuñeca=75
cantidadPayasoPedido=int(input('Cuantos payasos se vendieron en el ultimo pedido?'))
cantidadMuñePedido=int(input('Cuantas muñecas se vendieron en el ultimo pedido?'))
#pesoTotal=(pesoPayaso*cantidadPayasoPedido)+(cantidadMuñePedido*pesoMuñeca)
print(f'El paquete que sera enviado pesa: {(pesoPayaso*cantidadPayasoPedido)+(cantidadMuñePedido*pesoMuñeca)} gramos')

#Ejercicio 11
cajaDeAhorro=float(input('Introduce la cantidad de dinero que quiere ingresar a la caja de ahorro con 6% anual'))
interesAnual=0.06
anio1=cajaDeAhorro*interesAnual
anio2=anio1*interesAnual
anio3=anio2*interesAnual
print(f'El dinero que hay en la caja de ahorros es de:\n {cajaDeAhorro} \n -El primer año {anio1}\n -El segundo año {anio2} \n -El tercer anio {anio3}')

#Ejercicio 12
facturas=20
descuentoPorVencida=0,6
ventas=int(input('Cuantas facturas que no son del dia vendio hoy?'))
print(f'El precio habitual de la factura es de ${facturas}, el descuento que le hacemos es de ${facturas*descuentoPorVencida} por factura \n El total a pagar es de ${(facturas*ventas)*descuentoPorVencida}')

