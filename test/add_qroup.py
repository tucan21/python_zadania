# -*- coding: utf-8 -*-
from model.grupy import Grupy

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Grupy(name="grupa_1", header="qwerty", footer="qwerty"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Grupy(name="", header="", footer=""))
    app.session.logout()