def intermedio():
    num1=int(input('introduce el primer numero'))
    num2=int(input('introduce el segundo numero'))
    return (num1+num2)/2
def main():
    resultset=intermedio()
    print('El numero intermedio entre los 2 es:',resultset)
if __name__ == '__main__':
    main()