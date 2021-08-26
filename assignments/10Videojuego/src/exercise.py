def main():
    # escribe tu código abajo de esta línea
    pass
    juegos_nuevos = int(input("Dame la cantidad de juegos nuevos: "))
    juegos_usados = int(input("Dame la cantidad de juegos usados: "))
    costo_total = (juegos_nuevos*1000) + (juegos_usados*350)
    print(f'El total de la compra es: {costo_total}')


if __name__ == '__main__':
    main()
