def calcular_media(notas:list[float]) -> float:

    #validando se a lista é vazia
    if len(notas) == 0:
        raise ValueError("não é permitido uma lista vazia")
    
    media = sum(notas)/len(notas)
    return round(media,1)