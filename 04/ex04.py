def obter_resultados_vendas(vendedores: dict) -> dict:
    media = sum(vendedores.values()) / len(vendedores)
    media_75 = media * 0.75

    acima_media = []
    abaixo_media = []

    for (nome, valor) in vendedores.items():
        if valor < media_75:
            abaixo_media.append(nome)
        elif valor > media:
            acima_media.append(nome)

    return {
        "vendedores_acima_media": acima_media,
        "vendedores_abaixo_75_media": abaixo_media
    }
