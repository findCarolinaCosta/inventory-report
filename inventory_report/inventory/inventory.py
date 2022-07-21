import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def generate_by_csv(self, path):
        with open(path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=",")

            head, *data = csv_reader

        return [dict(zip(head, row)) for row in data]

    def report_by_type(self, data, type):
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)

    @classmethod
    def import_data(self, path, type):
        if path.endswith("csv"):
            data = self.generate_by_csv(path)

        print({type})
        return self.report_by_type(self, data, type)
