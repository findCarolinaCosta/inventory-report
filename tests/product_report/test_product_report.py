from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_do_produto = "produto"
    nome_da_empresa = "empresa"
    data_de_fabricacao = "01/01/0001"
    data_de_validade = "99/99/9999"
    numero_de_serie = "565151521"
    instrucoes_de_armazenamento = "sem"

    create_product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    relatorio = (
        f"O produto {nome_do_produto}"
        f" fabricado em {data_de_fabricacao}"
        f" por {nome_da_empresa} com validade"
        f" até {data_de_validade}"
        f" precisa ser armazenado {instrucoes_de_armazenamento}"
    )

    assert relatorio in str(create_product.__repr__)
