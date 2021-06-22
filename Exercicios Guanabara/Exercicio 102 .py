def fatorial(n1,show):
    """
    -> calucla o fatorial de um numero
    :param n1: o numero a ser calculado
    :param show:(opcional) mostrar ou não a conta
    :return:retorna a soma de todos os valores
    """
    s = 1
    j = n1
    for c in range(0,n1):
        s *= n1
        c+=1
        if show == True:
            if c < j:
                print(n1,end=' x ')
            elif c == j:
                print('1 =',end=' ')
        else:
            'ok'
        n1 -= 1
    print(s)


fatorial(5,show=False)