def area_rectangulo():
    altura=int(input('introduce cuantos cm tiene cada lado del rectangulo'))
    base=int(input('introduce cuantos cm tiene de base el rectangulo'))
    return altura*base
def main():
    resultset=area_rectangulo()
    print('el area del rectangulo tiene los siguientes cm:',resultset)
if __name__ == '__main__':
    main()
