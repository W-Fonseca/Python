def leiaint(num):
    while True:
        f = str(input(num))
        if f.isnumeric():
            p = int(f)
            return p
            break
        else:
            print('\033[0;31mErro: Não é um valor numerico!\033[m')


n = leiaint('digite um valor: ')
print(f'vocÊ acabou de digita o numero {n}')