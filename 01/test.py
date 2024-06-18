from ex01 import *


def test_extrair_posicoes_pares():
    entrada = [10, 15, 2, 21, 37, 4, 9, 13, 20, 31]
    saida = extrair_posicoes_pares(entrada)

    assert saida == [10, 2, 37, 9, 20]
