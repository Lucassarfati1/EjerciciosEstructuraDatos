def area_circulo():
    
    radio=int(input('introduce cuantos cm tiene de radio el circulo'))
    return radio*radio*3.14159
def main():
    resultset=area_circulo()
    print('el area del circulo tiene los siguientes cm:',resultset)
if __name__ == '__main__':
    main()