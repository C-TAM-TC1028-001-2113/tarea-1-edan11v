def main():
    # escribe tu código abajo de esta línea
    pass
    saldo_mes_anterior = float(input('Dame el saldo del mes anterior: '))
    ingresos = float(input('Dame los ingresos: '))
    egresos = float(input('Dame los egresos: '))
    num_cheques = float(input('Dame el número de cheques: '))
    balance = ( (num_cheques*13) + saldo_mes_anterior + ingresos - egresos ) 
    interes_banco = (balance*7.5)/100
    final=balance-interes_banco
    print(f'El saldo final de la cuenta es: {final}')

if __name__ == '__main__':
    main()
