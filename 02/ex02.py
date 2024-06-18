def gerar_lista(entrada: list) -> list:
    saida = []
    
    for (i, n) in enumerate(entrada):
        if i % 2 == 0:
            saida.append(n * 2)
        else:
            saida.append(n * 3)

    return saida
