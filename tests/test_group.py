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
    It should have an initial people of []
    """
    assert Group().count == 0
    assert Group().people == []


def test_add_people():
    """When I add (name, count) with add_people
    It should increment the count
    It should add the name, count to self.people
    """
    gr = Group()
    gr.add_people(("Toby and Enrique", 2))
    assert gr.count == 2
    assert ("Toby and Enrique", 2) in gr.people


def test_print_group(base_group, capsys):
    """When I call the display method
    It should print the names in people
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


def test_group_name_init():
    """When I create a group with kwarg name
    It should set the group name to that name
    """
    gr = Group(name="group 3")
    assert gr.name == "group 3"
