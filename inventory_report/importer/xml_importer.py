import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path, "r", encoding="utf-8") as file:
            return xmltodict.parse(file.read())["dataset"]["record"]
