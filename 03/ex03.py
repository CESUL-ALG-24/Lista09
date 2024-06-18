def obter_valor(atual: int, anterior: int) -> int:
    if atual % 2 == 0:
        return atual + anterior

    return atual - anterior


def obter_primeiro(n: int) -> int:
    if n % 2 == 0:
        return n + 2

    return n - 1


def transformar_lista(entrada: list) -> list:
    saida = []

    for i, n in enumerate(entrada):
        if i == 0:
            valor = obter_primeiro(n)
        else:
            valor = obter_valor(n, saida[i - 1])

        saida.append(valor)

    return saida
