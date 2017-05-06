from model.grupy import Grupy


def test_modify_first_group(app):
    app.group.test_modify_first_group(Grupy("qqq", "qqq", "qqq"))

