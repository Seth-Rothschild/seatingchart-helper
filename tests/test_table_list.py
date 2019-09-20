from tables.group import Group
from tables.table import Table
from tables.table_list import TableList
import pytest


@pytest.fixture
def base_table_list():
    gr1 = Group()
    gr1.add_people(("Steve and Eli", 2))
    gr1.set_name("group 1")

    gr2 = Group()
    gr2.set_name("group 2")
    tab1 = Table()
    tab1.add_group(gr1)
    tab1.set_name("table 1")
    tab2 = Table()
    tab2.set_name("table 2")
    tl = TableList()
    tl.groups = [gr2]
    tl.tables = [tab1, tab2]
    return tl


def test_tables():
    """When I initialize a table list
    It should have an attribute tables
    """
    tl = TableList()
    assert tl.tables == []
    assert tl.groups == []
    assert tl.raw == []


def test_export():
    """When I have a table list
    It should have an export method
    """
    tl = TableList()
    try:
        tl.export()
    except AttributeError:
        assert False


def test_csv():
    """When I run the read_csv method
    It should add the csv entries to raw
    """
    tl = TableList()
    tl.read_csv("tests/test_csv.csv")
    assert tl.raw[0] == ["Steve and Eli", "2"]


def test_init_with_csv():
    """When I run init with a csv
    It should add the csv entries to raw
    """
    tl = TableList(csv_path="tests/test_csv.csv")
    assert tl.raw[1] == ["Seth and Xavier", "2"]


def test_assign_group_by_name(base_table_list):
    """When I assign a group by name to table
    It should add that group to the table
    """
    tl = base_table_list
    tl.add("group 2", "table 2")
    assert len(tl.tables[1].groupslist) == 1
    assert len(tl.groups) == 0


def test_remove_group(base_table_list):
    """When I remove a group from a table
    It should remove the group from that table and add the group to the groups
    """
    tl = base_table_list
    tl.remove("group 1", "table 1")
    assert len(tl.tables[0].groupslist) == 0
    assert len(tl.groups) == 2
