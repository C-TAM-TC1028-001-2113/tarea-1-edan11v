def main():
    # escribe tu código abajo de esta línea
    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    pendiente = (y2-y1)/(x2-x1)
    print(f'Pendiente: {pendiente}')


if __name__ == '__main__':
    main()
