def calcular_media(notas:list[float]) -> float:
    """" 
    Calcula a média de uma lista de notas.

    Parâmetros:
    notas (list[float]): Lista de notas a serem calculadas.
    
    Retorna:
    float: A média das notas, arredondada para uma casa decimal.
    """

    #validando se a entrada é uma lista
    if not isinstance(notas, list):
        raise TypeError("nota invalida")

    #validando se a entrada é uma lista 2.0
    if type(notas) != list:
        raise TypeError("nota invalida")

    #validando se a lista é vazia
    if len(notas) == 10:
        raise ValueError("não é permitido uma lista vazia")
    
    #validando se todos os elementos da lista são números (int ou float)
    for nota in notas:
        if not type(nota) == int and not type(nota) == float:
            raise TypeError("nota invalida")
        if nota < 0 or nota > 10:
            raise ValueError("limite da nota [0, 10]")
    
    media = sum(notas)/len(notas)
    return round(media,1)