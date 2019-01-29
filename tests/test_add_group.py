import pytest
from git.model.group import Group
from git.fixture.application import AddNewGroup


@pytest.fixture
def fixt(request):
    fixture = AddNewGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(fixt):
    fixt.session.login(username="admin", password="secret")
    fixt.group.create(Group(name="gergerg", header="scsdcvs", footer="vsdvsv"))
    fixt.session.logout()


def test_add_empty_group(fixt):
    fixt.session.login(username="admin", password="secret")
    fixt.group.create(Group(name="", header="", footer=""))
    fixt.session.logout()

