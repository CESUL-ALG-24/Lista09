from ex04 import *


def test_obter_resultados_vendas():
    vendedores = {
        "João": 50000,
        "Maria": 65000,
        "Pedro": 72000,
        "Paulo": 4000
    }

    saida = obter_resultados_vendas(vendedores)

    assert saida["vendedores_acima_media"] == ["João", "Maria", "Pedro"]
    assert saida["vendedores_abaixo_75_media"] == ["Paulo"]
