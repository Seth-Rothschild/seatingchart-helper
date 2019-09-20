from tables.group import Group
import pytest


@pytest.fixture
def base_group():
    gr = Group()
    gr.add_people(("Steve and Eli", 2))
    return gr


def test_group_init():
    """When there is a group
    It should have an initial count of 0
    It should have an initial names of []
    """
    assert Group().count == 0
    assert Group().names == []
    assert Group().countlist == []


def test_add_people():
    """When I add (name, count) with add_people
    It should increment the count
    It should add the name to self.names
    It should add the count to countlist
    """
    gr = Group()
    gr.add_people(("Toby and Enrique", 2))
    assert gr.count == 2
    assert gr.countlist[0] == 2
    assert "Toby and Enrique" in gr.names


def test_print_group(base_group, capsys):
    """When I call the display method
    It should print the names in names
    """
    gr = base_group
    gr.display()
    captured = capsys.readouterr()
    assert "Steve and Eli" in captured.out


def test_group_name():
    """When I create a group
    It should have a name
    """
    gr = Group()
    assert gr.name == ""
    gr.set_name("group 1")
    assert gr.name == "group 1"
