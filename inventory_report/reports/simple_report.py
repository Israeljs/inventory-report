class SimpleReport:
    @staticmethod
    def earliest_manufacturing_date(products_list):
        earlest_date = [
            product["data_de_fabricacao"] for product in products_list
        ]
        return min(earlest_date)

    @staticmethod
    def nearest_expiration_date(products_list):
        nearest_date = [
            product["data_de_validade"] for product in products_list
        ]
        return min(nearest_date)

    @staticmethod
    def more_products_company(products_list):
        companies = [product["nome_da_empresa"] for product in products_list]
        return max(set(companies), key=companies.count)

    @staticmethod
    def generate(products):
        earliest_manufacturing = SimpleReport.earliest_manufacturing_date(
            products
        )
        nearest_expiration = SimpleReport.nearest_expiration_date(products)
        more_products_company = SimpleReport.more_products_company(products)

        return (
            f"Data de fabricação mais antiga: {earliest_manufacturing}\n"
            f"Data de validade mais próxima: {nearest_expiration}\n"
            f"Empresa com mais produtos: {more_products_company}"
        )
