def main():
    numbers = [22, 44, 93, 5, 25, 34, 78, 99, 87]

    mayor = None

    for num in numbers:
        if (mayor is None or num > mayor):
            mayor = num

    print('Maximo valor:',mayor)


if __name__ == '__main__':
    main()