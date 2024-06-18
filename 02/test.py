from ex02 import *


def test_gerar_lista():
    saida = gerar_lista([2, 3, 7, 10, 1])
    assert saida == [4, 9, 14, 30, 2]
