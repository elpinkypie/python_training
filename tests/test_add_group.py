import pytest
from git.model.group import Group
from git.fixture.application import AddNewGroup


@pytest.fixture
def fixt(request):
    fixture = AddNewGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(fixt):
    fixt.login(username="admin", password="secret")
    fixt.create_new_group(Group(name="gergerg", header="scsdcvs", footer="vsdvsv"))
    fixt.logout()


def test_add_emty_group(fixt):
    fixt.login(username="admin", password="secret")
    fixt.open_groups_page()
    fixt.logout()

