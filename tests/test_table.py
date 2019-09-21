from tables.table import Table
from tables.group import Group
import pytest


@pytest.fixture
def base_group():
    gr = Group()
    gr.add_people(("Steve and Eli", 2))
    return gr


@pytest.fixture
def base_table():
    gr = Group()
    gr.add_people(("Steve and Eli", 2))
    tab = Table(name="Table 1")
    tab.add_group(gr)
    return tab


def test_table_init():
    """When a table is initialized
    It should have a count of 0
    It should have a groups of []
    """
    assert Table().count == 0
    assert Table().groups == []


def test_add_group_to_table(base_group):
    """When I add a group to a table
    It should add the group to groups
    It should add the count of the group to count
    """
    gr = base_group
    tab1 = Table()
    tab1.add_group(gr)
    assert tab1.count == 2
    assert tab1.groups[0] == gr


def test_remove_group_from_table(base_group):
    """When I remove a group from the table
    It should remove the group from groups
    and it should decrement the count
    """
    gr = base_group
    tab1 = Table()
    tab1.add_group(gr)
    tab1.remove_group(gr)
    assert tab1.count == 0
    assert tab1.groups == []


def test_print_table(base_table, capsys):
    """When a run print table
    It should give people in the groups at the table
    It should print the current table count
    """
    tab1 = base_table
    tab1.display()
    captured = capsys.readouterr()
    assert "Steve and Eli" in captured.out
    assert "2" in captured.out


def test_table_maximum():
    """When a table is initialized
    It should have a maximum capacity
    It should be configurable via kwarg
    """
    tab1 = Table()
    tab2 = Table(capacity=8)
    assert tab1.capacity == 12
    assert tab2.capacity == 8


def test_num_remaining(base_group):
    """When a table is modified
    It should alter self.remaining using count and capacity
    """
    gr = base_group
    tab = Table()
    tab.add_group(gr)
    assert tab.remaining == 10
    tab.remove_group(gr)
    assert tab.remaining == 12


def test_overflow():
    """When I try to add too many people to a table
    It should fail silently
    """
    gr = Group()
    gr.add_people(("", 13))
    tab = Table()
    tab.add_group(gr)
    assert tab.count == 0
    assert len(tab.groups) == 0


def test_invalid_remove(base_group):
    """When I try to remove a group not in the groups
    It should fail silently
    """
    gr = base_group
    tab = Table()
    tab.remove_group(gr)
    assert tab.count == 0


def test_table_name():
    """When I create a table
    It should have a name
    """
    tab = Table()
    assert tab.name == ""
    tab.set_name("table 1")
    assert tab.name == "table 1"


def test_table_name_init():
    """When I initialize with a name kwarg
    It should set table name to that argument
    """
    tab = Table(name="table 1")
    assert tab.name == "table 1"
