from tables.group import Group
from tables.table import Table
from tables import Arrangement
import pytest


@pytest.fixture
def base_table_list():
    gr1 = Group(name="group 1")
    gr1.add_people(("Steve and Eli", 2))

    gr2 = Group(name="group 2")
    tab1 = Table(name="table 1")
    tab1.add_group(gr1)

    tab2 = Table(name="table 2")
    arr = Arrangement()
    arr.groups = [gr2]
    arr.tables = [tab1, tab2]
    return arr


def test_tables():
    """When I initialize a table list
    It should have an attribute tables
    """
    arr = Arrangement()
    assert arr.tables == []
    assert arr.groups == []
    assert arr.raw == []


def test_export(base_table_list):
    """When I have a table list
    It should have an export method
    It should write names, count, group name and table name
    """
    arr = base_table_list
    arr.export("tests/output.csv")
    arr.read_csv("tests/output.csv")
    assert arr.raw[0] == ["Steve and Eli", "2", "group 1", "table 1"]


def test_csv():
    """When I run the read_csv method
    It should add the csv entries to raw
    """
    arr = Arrangement()
    arr.read_csv("tests/test_csv.csv")
    assert arr.raw[0] == ["Steve and Eli", "2"]


def test_init_with_csv():
    """When I run init with a csv
    It should add the csv entries to raw
    """
    arr = Arrangement(csv_path="tests/test_csv.csv")
    assert arr.raw[1] == ["Seth and Xavier", "2"]


def test_assign_group_by_name(base_table_list):
    """When I assign a group by name to table
    It should add that group to the table
    """
    arr = base_table_list
    arr.add("group 2", "table 2")
    assert len(arr.tables[1].groupslist) == 1
    assert len(arr.groups) == 0


def test_remove_group(base_table_list):
    """When I remove a group from a table
    It should remove the group from that table and add the group to the groups
    """
    arr = base_table_list
    arr.remove("group 1", "table 1")
    assert len(arr.tables[0].groupslist) == 0
    assert len(arr.groups) == 2
