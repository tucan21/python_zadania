# -*- coding: utf-8 -*-
from model.grupy import Grupy


def test_add_group(app):
    app.group.test_add_group(Grupy(name="qwerty", header="qwerty", footer="qwerty"))

def test_add_empty_group(app):
    app.group.test_add_group(Grupy(name="", header="", footer=""))
