a = str(input('digite uma frase e direi se ela é palindromo:'))
b = list(a.replace(' ',''))
s = list(reversed(b))
if b == s:
    print('sim')
elif b != s:
    print('nao')
print('fim')