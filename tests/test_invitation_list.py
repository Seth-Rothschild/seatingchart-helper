from tables.invitation_list import InvitationList


def test_raw():
    """When I initialize a grouplist
    It should have an attribute 'raw'
    """
    il = InvitationList()
    assert il.raw == []


def test_csv():
    """When I run the read_csv method
    It should add the csv entries to raw
    """
    il = InvitationList()
    il.read_csv("tests/test_csv.csv")
    assert il.raw[0] == ("Steve and Eli", 2)


def test_init_with_csv():
    """When I run init with a csv
    It should add the csv entries to raw
    """
    il = InvitationList(csv_path="tests/test_csv.csv")
    assert il.raw[1] == ("Seth and Xavier", 2)
