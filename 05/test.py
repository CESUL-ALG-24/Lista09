from ex05 import *


def test_obter_lista_compra():
    produtos = [
        {"nome": "carne", "valor": 35, "qtde": 3},
        {"nome": "arroz", "valor": 40, "qtde": 1},
        {"nome": "feijão", "valor": 12, "qtde": 2},
    ]

    saida = obter_totais_compra(produtos)

    assert saida == {
        "produtos": [
            {"nome": "carne", "valor": 35, "qtde": 3, "total": 105},
            {"nome": "arroz", "valor": 40, "qtde": 1, "total": 40},
            {"nome": "feijão", "valor": 12, "qtde": 2, "total": 24},
        ],
        "total": 169
    }
