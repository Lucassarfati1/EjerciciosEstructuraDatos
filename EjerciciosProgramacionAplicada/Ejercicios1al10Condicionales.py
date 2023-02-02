#Ejercicio 1
edad=int(input('Ingrese su edad'))
if(edad>=18):
    print('Usted es mayor de edad')
else:
    print('usted es menor de edad')

#Ejercicio 2
contraseñaOk='contraseña'
contraseña=input('Introduzca la contraseña')
contraseña.lower()
if(contraseña==contraseñaOk):

    print(f'La contraseña "{contraseña}" es correcta')
else:
    print(f'La contraseña "{contraseña}" es incorrecta')

#Ejercicio 3
num1=int(input('Ingrese el numero dividendo'))
num2=int(input('Ingrese el numero divisor'))
resultado=num1/num2
if(num2>=1):
    print(f'El resultado de la operacion es {resultado}')
else:
    print('ERROR No se puede dividir por 0 ni por numeros negativos ')

#Ejercicio 4
numero=int(input('Ingrese un numero para saber si es par'))
if(numero%2==0):
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')

#Ejercicio 5
tributar=False
edad=int(input('Ingrese su edad'))
ingresos=float(input('Ingrese sus ingresos mensuales'))
if(ingresos>=360000 and edad>16):
    print('Usted debe pagar el tributo ya que cumple con los requisitos')
else:
    print('Usted no debe pagar el tributo')

#Ejercicio 6
nombre=input('Introduzca su nombre')
sexo=input('Introduzca su sexo M (masculino) o F (Femenino)')
sexo.upper()
if (sexo == "M" and nombre.lower() > 'n') or (sexo == "F" and nombre.lower() < 'm'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)

#Ejercicio 7
renta=int(input('Cual es el valor de su renta anual'))
if(renta<100000):
    print(f'Su valor impositivo es del 5% serian ${renta*0.05}')
elif(renta>=100000 and renta<200000):
    print(f'Su valor impositivo es del 15% serian ${renta*0.15}')
elif(renta>=200000 and renta <350000 ):
    print(f'Su valor impositivo es del 20% serian ${renta*0.2}')
elif(renta>=350000 and renta <600000):
    print(f'Su valor impositivo es del 30% serian ${renta*0.3}')
elif(renta>=600000):
    print(f'Su valor impositivo es del 45% serian ${renta*0.45}')

#Ejercicio 8
inaceptable=0.0
aceptable=0.4
meritorio=0.6
puntos=float(input('Indique la puntuacion del empleado, los opciones son inaceptable(0.0), aceptable(0.4) meritorio(0.6) o mas'))
if(puntos==inaceptable):
    print(f'Su nivel de rendimiento es INACEPTABLE debido a su puntuacion {puntos} y le corresponde cobrar ${inaceptable*20400}')
elif(puntos==aceptable):
    print(f'Su nivel de rendimiento es ACEPTABLE debido a su puntuacion {puntos} y le corresponde cobrar ${aceptable*20400}')
elif(puntos==meritorio or puntos>meritorio):
    print(f'Su nivel de rendimiento es  MERITORIO debido a su puntuacion {puntos} y le corresponde cobrar ${meritorio*20400}')

#Ejercicio 9
edad=int(input('Que edad tiene?'))
if(edad<4):
    print('Puede entrar gratis porque eres un niño pequeño que no tiene ni 4 años')
elif(edad>3 and edad<18):
    print('Usted debe pagar $500 porque tiene entre 4 y 18 años de edad')
elif(edad>=18):
    print('Usted debe pagar $1000 porque es mayor de edad')

#Ejercicio 10
pimiento='Pimiento'
tofu='Tofu'
peperoni='Peperoni'
jamon='Jamón'
salmon='Sálmon'
vegetariano=False

pizza=input('Señor cliente usted quiere una pizza vegetariana?')
pizza.lower()
if(pizza=='si'):
    vegetariano=True
    ingrediente=input(f'Los ingredientes que le puede agregar a la pizza vegetariana son {tofu} o {pimiento} ¿Cual va a elegir?')
    ingrediente.lower()
    if(ingrediente=='tofu'):
        print(f'Aqui esta su pedido sr cliente:\n -Pizza vegetariana de muzzarella con tomate y el ingrediente agregado es el {tofu}')
    elif(ingrediente=='pimiento'):
        print(f'Aqui esta su pedido sr cliente:\n -Pizza vegetariana de muzzarella con tomate y el ingrediente agregado es el {pimiento}')
elif(pizza=='no'):
    ingrediente=input(f'Los ingredientes que le puede agregar a la pizza NO vegetariana son {peperoni}, {jamon} o {salmon}')
    ingrediente.lower()
    if(ingrediente=='peperoni'):
        print(f'Aqui esta su pedido sr cliente:\n -Pizza NO vegetariana de muzzarella con tomate y el ingrediente agregado es el {peperoni}')
    elif(ingrediente=='jamon'):
        print(f'Aqui esta su pedido sr cliente:\n -Pizza NO vegetariana de muzzarella con tomate y el ingrediente agregado es el {jamon}')
    elif(ingrediente=='salmon'):
        print(f'Aqui esta su pedido sr cliente:\n -Pizza NO vegetariana de muzzarella con tomate y el ingrediente agregado es el {salmon}')


