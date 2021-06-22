def voto(num):
    s = 2020 - num
    if s >=18 and s <=65:
        return print(f'com {s} anos: O voto é obrigatorio!')
    elif s >=65:
        return print(f'com {s} anos: O voto é opcional')
    elif s <18:
        return print(f'com {s} anos: Não pode votar!')


voto(int(input('Digite o ano de nascimento')))