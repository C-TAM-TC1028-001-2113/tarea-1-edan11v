def main():
    # escribe tu código abajo de esta línea
    pass
    mensajes = float(input("Dame el número de mensajes: "))
    megas = float(input('Dame el número de megas: '))
    minutos = float(input('Dame el número de minutos: '))
    costo_mensual = ((mensajes+megas+minutos)*0.80)
    print(f'El costo mensual es: {costo_mensual}')


if __name__ == '__main__':
    main()
