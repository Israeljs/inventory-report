
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type):
        self.data += self.importer.import_data(path)

        if report_type == "simples":
            return SimpleReport.generate(self.data)
        return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)