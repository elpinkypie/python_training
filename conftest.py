import pytest
from git.fixture.application import Application


@pytest.fixture(scope="session")
def fixt(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
