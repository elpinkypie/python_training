import pytest
from git.tests.group import Group
from git.tests.application import Application


@pytest.fixture
def fixt(request):
    fixture = Application()
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

