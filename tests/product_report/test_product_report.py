from inventory_report.inventory.product import Product


def test_relatorio_produto():
    productMock = Product(
        13,
        "Course",
        "Trybe",
        "01-01-2020",
        "01-01-2050",
        "hyw93jk",
        "Online Web"
    )

    assert productMock.__repr__() == (
        f"O produto {productMock.nome_do_produto} "
        f"fabricado em {productMock.data_de_fabricacao} "
        f"por {productMock.nome_da_empresa} com validade "
        f"até {productMock.data_de_validade} "
        f"precisa ser armazenado {productMock.instrucoes_de_armazenamento}."
    )
    assert type(productMock.__repr__()) == str
