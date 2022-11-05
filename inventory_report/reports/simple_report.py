from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def old_date(cls, list):
        return min(
            datetime.fromisoformat(item["data_de_fabricacao"]).date()
            for item in list
        )

    @classmethod
    def close_date(cls, list):
        return min(
            datetime.fromisoformat(item["data_de_validade"]).date()
            for item in list
            if datetime.fromisoformat(item["data_de_validade"])
            > datetime.now()
        )

    @classmethod
    def enterprise(cls, list):
        return Counter(
            [item["nome_da_empresa"] for item in list]
        ).most_common()[0][0]

    @classmethod
    def generate(cls, list):
        old = SimpleReport.old_date(list)
        close = SimpleReport.close_date(list)
        products = SimpleReport.enterprise(list)

        return (
            f"Data de fabricação mais antiga: {old}\n"
            f"Data de validade mais próxima: {close}\n"
            f"Empresa com mais produtos: {products}"
        )
