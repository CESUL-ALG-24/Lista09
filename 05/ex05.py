def obter_totais_compra(produtos: list) -> dict:
    lista_compra = []
    total = 0

    for produto in produtos:
        produto["total"] = produto["qtde"] * produto["valor"]
        total += produto["total"]
        lista_compra.append(produto)

    return {
        "produtos": lista_compra,
        "total": total
    }
