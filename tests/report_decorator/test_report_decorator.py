from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

products = [
    {
        "id": "1",
        "nome_do_produto": "produto",
        "nome_da_empresa": "empresa",
        "data_de_fabricacao": "01/01/0001",
        "data_de_validade": "99/99/9999",
        "numero_de_serie": "565151521",
        "instrucoes_de_armazenamento": "sem",
    }
]


def test_decorar_relatorio():
    result = (
        "\x1b[32mData de fabricação mais antiga:\x1b[0m 01/01/0001\n"
        + "\x1b[32mData de validade mais próxima:\x1b[0m 99/99/9999\n"
        + "\x1b[32mEmpresa com mais produtos:\x1b[0m \x1b[31mempresa\x1b[0m"
    )

    assert result == ColoredReport(SimpleReport).generate(products)
