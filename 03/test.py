from ex03 import *


def test_obter_valor_atual_par():
    valor = obter_valor(2, 3)
    assert valor == 5


def test_obter_valor_atual_impar():
    valor = obter_valor(3, 1)
    assert valor == 2


def test_obter_primeiro_par():
    valor = obter_primeiro(4)
    assert valor == 6


def test_obter_primeiro_impar():
    valor = obter_primeiro(1)
    assert valor == 0


def test_transformar_lista():
    saida = transformar_lista([15, 8, 12, 9, 20])
    assert saida == [14, 22, 34, -25, -5]
