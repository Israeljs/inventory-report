from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 100
    nome_do_produto = "Feijão"
    nome_da_empresa = "Feijoaras ltd"
    data_de_fabricacao = "05/07/2022"
    data_de_validade = "05/07/2023"
    numero_de_serie = "GTD524HY2022"
    instrucoes_de_armazenamento = "Conservar em local fresco e arejado"

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    message = (
        f"O produto {nome_do_produto}"
        f" fabricado em {data_de_fabricacao}"
        f" por {nome_da_empresa} com validade"
        f" até {data_de_validade}"
        f" precisa ser armazenado {instrucoes_de_armazenamento}."
    )

    assert repr(product) == message
