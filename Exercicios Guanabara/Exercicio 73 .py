fut = ('flamengo','atletico-mg','vasco','palmeiras','bota fogo','bahia','santos','bragantino','corinthians','atletico-go','gremio','fluminence','sport','ceara','coritiba','internacional','fortaleza','athletico','goias','sao paulo')
print(fut[0:5])
print(fut[-4:20])
print(sorted(fut))
if fut == 'chapecoense':
    print(fut.index('chapecoense'))
else:
    print('Não existe chapecoense na lista')