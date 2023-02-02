def main():
    mail=input('Ingrese un mail')
    if(mail.find('@')!=-1):
        print('Se ha ingresado un mail correctamente. El mail es:',mail)
    else:
            print('No se ha podido ingresar el mail porque no tiene ningun @, intentelo devuelta')
if __name__ == '__main__':
    main()