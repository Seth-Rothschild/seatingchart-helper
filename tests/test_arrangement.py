from tables.group import Group
from tables.table import Table
from tables import Arrangement
import pytest
import os


@pytest.fixture
def arr_with_raw():
    arr = Arrangement()
    arr.raw = [
        ["p1", "1", "group 1", ""],
        ["p2", "2", "group 2", ""],
        ["p3", "3", "group 1", ""],
        ["p4", "4", "", ""],
        ["p5", "5", "group 5", "table 5"],
    ]
    return arr


@pytest.fixture
def base_arrangement():
    gr1 = Group(name="group 1")
    gr1.add_people(("Steve and Eli", 2))

    gr2 = Group(name="group 2")
    tab1 = Table(name="table 1")
    tab1.add_group(gr1)

    tab2 = Table(name="table 2")
    arr = Arrangement()
    arr.unseated = [gr2]
    arr.tables = [tab1, tab2]
    return arr


def test_tables():
    """When I initialize a table list
    It should have an attribute tables
    """
    arr = Arrangement()
    assert arr.tables == []
    assert arr.unseated == []
    assert arr.raw == []


def test_export(base_arrangement):
    """When I have a table list
    It should have an export method
    It should write names, count, group name and table name
    """
    path = "tests/output.csv"
    arr = base_arrangement
    arr.export(path)
    arr.read_csv(path)
    assert arr.raw[0] == ["Steve and Eli", "2", "group 1", "table 1"]
    os.remove(path)


def test_csv():
    """When I run the read_csv method
    It should add the csv entries to raw
    It should add unseated groups to unseated
    It should add the seated groups to their table
    """
    arr = Arrangement(csv_path="tests/test.csv")
    assert arr.raw[0] == ["Steve and Eli", "2", "creep slayerz", ""]
    assert arr.raw[1] == ["Seth and Xavier", "2", "group 1", "table 1"]
    names = [gr.name for gr in arr.unseated]
    assert "creep slayerz" in names

    print([tab.name for tab in arr.tables])
    assert len(arr.tables) == 1
    assert arr.tables[0].name == "table 1"
    assert arr.tables[0].groups[0].name == "group 1"


def test_assign_group_by_name(base_arrangement):
    """When I assign a group by name to table
    It should add that group to the table
    """
    arr = base_arrangement
    arr.add("group 2", "table 2")
    assert len(arr.tables[1].groups) == 1
    assert len(arr.unseated) == 0


def test_find_unseated_group(base_arrangement):
    """When I look for a group in unseated
    It should return a single group of the same name
    """
    gr2 = base_arrangement._find_unseated_group("group 2")
    assert gr2.name == "group 2"


def test_remove_group(base_arrangement):
    """When I remove a group from a table
    It should remove the group from that table and add to unseated
    """
    arr = base_arrangement
    arr.remove("group 1")
    assert len(arr.tables[0].groups) == 0
    assert len(arr.unseated) == 2


def test_create_groups_from_raw(arr_with_raw):
    """When I create groups from raw
    It should create groups for every name
    It should populate those groups with the names from raw
    It should make new groups from blank group names
    """
    arr = arr_with_raw
    arr._create_groups_from_raw()
    assert len(arr.unseated) == 4
    for group in arr.unseated:
        if group.name == "group 1":
            assert ("p1", 1) in group.people
            assert ("p3", 3) in group.people
        elif group.name == "group 2":
            assert ("p2", 2) in group.people
        elif group.name == "p4":
            assert ("p4", 4) in group.people


def test_create_tables_from_raw(arr_with_raw):
    """When I create tables from raw
    It should generate tables of the names in raw
    """
    raw = arr_with_raw
    raw._create_tables_from_raw()
    assert len(raw.tables) == 1
    assert raw.tables[0].name == "table 5"


def test_display(base_arrangement, capsys):
    """When I display an arrangement
    It should display table for each table
    It should display unassigned
    """
    base_arrangement.display()
    captured = capsys.readouterr()
    assert "table 1" in captured.out
    assert "Steve and Eli" in captured.out
    assert "Unseated" in captured.out
