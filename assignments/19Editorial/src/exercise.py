def main():
    # escribe tu código abajo de esta línea
    pass
    from math import ceil
    num_palabras = int(input('Dame el número de palabras: '))
    if num_palabras<=475:
        costo = 54
        print(f'El costo de la publicación es: {costo}')
    else:
        paginas = float(num_palabras)/475
        total_pag = int(ceil(paginas))
        costo = float(total_pag*54)
        print(f'El costo de la publicación es: {costo}')


if __name__ == '__main__':
    main()
