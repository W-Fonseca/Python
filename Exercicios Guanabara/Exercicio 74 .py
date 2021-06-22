f = []
from random import choices
a = 0,1,2,3,4,5,6,7,8,9,10
for n in range (0,5):
    b = choices(a)
    f += b
print(f'os numeros sorteados foram {f}',)
print(f'o maior numero é {max(f)}')
print(f'O menor numero é {min(f)}')