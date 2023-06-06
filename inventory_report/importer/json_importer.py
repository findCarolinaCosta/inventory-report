import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        with open(path, "r", encoding="utf-8") as file:
            return [data for data in json.load(file)]
