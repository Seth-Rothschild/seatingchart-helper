import tables


def test_tables_name():
    """When tables is installed
    It should have a __name__ attribute
    """
    assert tables.__name__ == "tables"
