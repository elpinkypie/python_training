import pytest
from git.fixture.application import Application


@pytest.fixture(scope="session")
def fixt(request):
    fixture = Application()
    fixture.session.login(username="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
