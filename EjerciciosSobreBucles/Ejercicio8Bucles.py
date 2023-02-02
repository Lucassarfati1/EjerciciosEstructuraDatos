def main():
    numbers = [22, 44, 93, 5, 25, 34, 78, 99, 87]

    menor = None

    for num in numbers:
        if (menor is None or num < menor):
            menor = num

    print('Minimo valor:',menor)


if __name__ == '__main__':
    main()