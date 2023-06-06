import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import json
import xmltodict


class Inventory:
    @classmethod
    def generate_by_csv(self, path):
        with open(path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=",")

            head, *data = csv_reader

        return [dict(zip(head, row)) for row in data]

    def generate_by_json(path):
        with open(path, "r", encoding="utf-8") as file:

            return json.load(file)

    def generate_by_xml(self, path):
        with open(path, "r", encoding="utf-8") as file:

            return xmltodict.parse(file.read())["dataset"]["record"]

    def report_by_type(self, data, type):
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)

    @classmethod
    def import_data(self, path, type):
        if path.endswith("csv"):
            data = self.generate_by_csv(path)

        if path.endswith("json"):
            data = self.generate_by_json(path)

        if path.endswith("xml"):
            data = self.generate_by_xml(self, path)

        return self.report_by_type(self, data, type)
