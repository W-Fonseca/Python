frase = str.strip(input('Digite uma frase: ')).upper()
frase2 = str(frase.count('A'))
Add = '1'+frase
frase3 = Add.find('A')
frase4 = Add.rfind('A')
print('Quantidade de letras A são: {}'.format(frase2))
print('A primeira Letra A apareceu na posição: {}'.format(frase3))
print('Ultima letra A esta localizada na Posição {}'.format(frase4))

