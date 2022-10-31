def recortar(num, lim_inf, lim_sup):
    return max(min(num, lim_sup), lim_inf)
def main():
    resultset=recortar(23,10,50)
    print('El numero recortado es:',resultset)
if __name__ == '__main__':
    main()