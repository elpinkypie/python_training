# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_group(app):
    app.login(username="admin", password="secret")
    app.create_new_group(Group(name="gergerg", header="scsdcvs", footer="vsdvsv"))
    app.logout()

def test_add_emty_group(app):
    app.login(username="admin", password="secret")
    app.open_groups_page()
    app.logout()

