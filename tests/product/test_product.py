from inventory_report.inventory.product import Product


def test_cria_produto():
    create_product = Product(
        "1",
        "nome do produto",
        "nome da empresa",
        "01/01/0001",
        "99/99/9999",
        "565151521",
        "sem instrução",
    )
    assert create_product.id == "1"
    assert create_product.data_de_validade == "99/99/9999"
    assert create_product.instrucoes_de_armazenamento == "sem instrução"
