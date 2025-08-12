import pytest
from escola.aluno import calcular_media

def test_calcular_media_lista_vazia():
    #Definindo a entrada
    entrada = []

    #Executando a função e esperando erro
    with pytest.raises(ValueError, match="não é permitido uma lista vazia"):
        calcular_media(entrada)



def test_calcular_media_enviando_string():
    #Definindo a entrada
    entrada = "ola"

    #Executando a função e esperando erro
    with pytest.raises(TypeError, match="nota invalida"):
        calcular_media(entrada)


def test_calcular_media_com_numero_negativo():
    #Definindo a entrada
    entrada = [-10.0]

    #Executando a função e esperando erro
    with pytest.raises(ValueError, match="limite da nota \[0, 10\]"):
        calcular_media(entrada)

def test_calcular_media_com_numero_maior_que_10():
    #Definindo a entrada
    entrada = [8,10,11]

    #Executando a função e esperando erro
    with pytest.raises(ValueError, match="limite da nota \[0, 10\]"):
        calcular_media(entrada)