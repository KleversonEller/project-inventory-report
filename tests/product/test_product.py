from inventory_report.inventory.product import Product


def test_cria_produto():
    productMock = Product(
        13,
        "Course",
        "Trybe",
        "01-01-2020",
        "01-01-2050",
        "hyw93jk",
        "Online Web"
    )

    assert type(productMock.id) == int
    assert type(productMock.nome_da_empresa) == str
    assert type(productMock.nome_do_produto) == str
    assert type(productMock.data_de_fabricacao) == str
    assert type(productMock.data_de_validade) == str
    assert type(productMock.numero_de_serie) == str
    assert type(productMock.instrucoes_de_armazenamento) == str
    assert productMock.id == 13
    assert productMock.nome_da_empresa == "Trybe"
    assert productMock.nome_do_produto == "Course"
    assert productMock.data_de_fabricacao == "01-01-2020"
    assert productMock.data_de_validade == "01-01-2050"
    assert productMock.numero_de_serie == "hyw93jk"
    assert productMock.instrucoes_de_armazenamento == "Online Web"
