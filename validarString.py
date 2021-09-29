def validar(texto):
    import re
    lista_Componentes = []
    data = re.findall("[\d]{1,2}(?:.|/|\|)[\d]{1,2}(?:.|/|\|)[\d]{2,4}", texto)
    print(data)
    print(texto)
    quantidade = texto.count("[")

    for c in range(0, quantidade):
        local1 = texto.index("[")
        local2 = texto.index("]")
        item = texto[local1:local2+1].replace("[","").replace("]","")
        print(item)
        lista_Componentes += [item]
        print(lista_Componentes)
        texto = texto.replace(texto[local1:local2+1],"")

  #https://regex101.com/r/F7t55q/6


validar("[RFQ]_[COUPA]_[28.09.2021]_[EFA]_1")
