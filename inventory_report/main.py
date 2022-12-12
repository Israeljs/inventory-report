
import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.csv_importer import CsvImporter


def main():
    try:
        file_path, report_type = sys.argv[1], sys.argv[2]
        importer_class = ""
        if file_path.endswith("json"):
            importer_class = JsonImporter
        elif file_path.endswith("xml"):
            importer_class = XmlImporter
        else:
            importer_class = CsvImporter
        report = InventoryRefactor(importer_class)
        sys.stdout.write(report.import_data(file_path, report_type))
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")
