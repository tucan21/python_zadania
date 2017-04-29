# -*- coding: utf-8 -*-
import pytest
from fixture.aplikacja_grupy import Aplikacja_grupy
from model.grupy import Grupy


@pytest.fixture
def app(request):
    fixture = Aplikacja_grupy()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_form(Grupy(name="grupa_1", header="qwerty", footer="qwerty"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_form(Grupy(name="", header="", footer=""))
    app.session.logout()