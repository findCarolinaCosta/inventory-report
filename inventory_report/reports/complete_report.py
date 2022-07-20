from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def __getProductsByCompany(self, companies):
        result = ""
        for company in companies.most_common():
            result += f"- {company[0]}: {company[1]}\n"

        return f"{result}"

    @classmethod
    def generate(self, report):
        companies = Counter([company["nome_da_empresa"] for company in report])
        return (
            f"{super().generate(report)}\n"
            "Produtos estocados por empresa:\n"
            f"{self.__getProductsByCompany(companies)}"
        )
