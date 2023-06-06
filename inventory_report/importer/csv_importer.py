import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=",")

            head, *data = csv_reader

            return [dict(zip(head, row)) for row in data]
