def sumaRecursiva(num):
    if(num==0):
        return 0
    else:
        return num+sumaRecursiva(num-1)

def main():
    print(sumaRecursiva(5))
if __name__ == '__main__':
    main()