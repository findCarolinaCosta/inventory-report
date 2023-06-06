class filterReport:
    @classmethod
    def getOldestManufacture(self, report):
        return min([date["data_de_fabricacao"] for date in report])

    @classmethod
    def getClosestExpirationDate(self, report):
        return min([date["data_de_validade"] for date in report])

    @classmethod
    def getCompanyWithMoreProducts(self, report):
        companies = [company["nome_da_empresa"] for company in report]
        countProduct = companies.count
        return max(companies, key=countProduct)


class SimpleReport:
    @classmethod
    def generate(self, report):
        oldest_date = filterReport.getOldestManufacture(report)
        closest_date = filterReport.getClosestExpirationDate(report)
        company_bigger_stock = filterReport.getCompanyWithMoreProducts(report)
        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )
