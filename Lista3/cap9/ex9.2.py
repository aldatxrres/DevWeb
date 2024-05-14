def calculaMedia(lista):
    try:
        if len(lista) == 0:
            raise ValueError("A lista está vazia")
        
        soma = 0
        contador = 0
        for numero in lista:
            if not isinstance(numero, (int, float)):
                raise TypeError("Há valores não numéricos na lista")
            soma += numero
            contador += 1
        
        media = soma / contador
        return media
    
    except ValueError as ve:
        print(ve)
    
    except TypeError as te:
        print(te)