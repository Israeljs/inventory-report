from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def count_products(list_products):
        products = {}

        for product in list_products:
            company = product["nome_da_empresa"]
            if company not in products:
                products[company] = 1
            else:
                products[company] += 1
        return products

    @staticmethod
    def generate(list_products):
        simple_report = SimpleReport.generate(list_products)
        amount = CompleteReport.count_products(list_products)
        items = amount.items()
        products = ""

        for company, quantity in items:
            products += f"- {company}: {quantity}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{products}"
        )
