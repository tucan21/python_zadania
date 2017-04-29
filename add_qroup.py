# -*- coding: utf-8 -*-
import pytest
from grupy import Grupy
from aplikacja_grupy import Aplikacja_grupy


@pytest.fixture
def app(request):
    fixture = Aplikacja_grupy()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group(app):
    success = True
    app.login(username="admin", password="secret")
    app.fill_form(Grupy(name="grupa_1", header="qwerty", footer="qwerty"))
    app.logout()


def test_add_empty_group(app):
    success = True
    app.login(username="admin", password="secret")
    app.fill_form(Grupy(name="", header="", footer=""))
    app.logout()
