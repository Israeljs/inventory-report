import csv
import json
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        report = ''
        product_data = []

        if path.endswith('csv'):
            product_data = Inventory.readCSV(path)
        elif path.endswith('json'):
            product_data = Inventory.readJSON(path)
        elif path.endswith('xml'):
            product_data = Inventory.readXML(path)
        else:
            raise ValueError("Invalid value")

        simple_report = SimpleReport.generate(product_data)
        complete_report = CompleteReport.generate(product_data)

        if report_type == 'simples':
            report = simple_report
        else:
            report = complete_report
        return report

    @staticmethod
    def readCSV(path):
        with open(path) as file:
            return list(csv.DictReader(file))

    @staticmethod
    def readJSON(path):
        with open(path) as file:
            return json.loads(file.read())

    @classmethod
    def readXML(cls, path):
        with open(path) as file:
            return xmltodict.parse(file.read())["dataset"]["record"]
