from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def products_store(cls, list):
        result = ""

        products = Counter(
            [item["nome_da_empresa"] for item in list]
        )

        for enterprise, qty in products.items():
            result += f"- {enterprise}: {qty}\n"

        return result

    @classmethod
    def generate(cls, list):
        products = CompleteReport.products_store(list)

        return (
            super().generate(list)
            + "\nProdutos estocados por empresa:\n"
            + products
        )
