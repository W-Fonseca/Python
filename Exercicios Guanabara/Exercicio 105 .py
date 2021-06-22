def notas(*num,sit):
    """
    ->Função para analisar notas de varios alunos.
    :param num:notas dos alunos(aceita varias)
    :param sit:valor opcional(True ou False) adiciona situação
    :return:lista com varias situações da turma
    """
    z = []
    f = len(num)
    s = max(num)
    a = min(num)
    b = sum(num) / f
    if b > 5:
        x = 'Situação: BOA!'
    elif b < 5:
        x = 'Situação: RUIM!'
    elif b == 5:
        x = 'Situação: MÉDIA'
    z += [f,s,a,b,x]
    if sit == True:
        print(f'total: {z[0]}, Maior: {z[1]}, Menor: {z[2]}, média {z[3]}, {z[4]}')
    elif sit == False:
        print(f'total: {z[0]}, Maior: {z[1]}, Menor: {z[2]}, média {z[3]}')


resp = notas(5,9.5,2,3.5,sit=True)