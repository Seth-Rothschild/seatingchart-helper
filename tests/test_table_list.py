from tables.table_list import TableList


def test_tables():
    """When I initialize a table list
    It should have an attribute tables
    """
    tl = TableList()
    assert tl.tables == []


def test_export():
    """When I have a table list
    It should have an export method
    """
    tl = TableList()
    try:
        tl.export()
    except AttributeError:
        assert False
    

