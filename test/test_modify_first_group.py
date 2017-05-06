from model.grupy import Grupy


def test_modify_first_group(app):
   app.group.test_modify_first_group(Grupy("qqq", "qqq", "qqq"))

def test_modify_group_name(app):
    app.group.test_modify_first_group(Grupy(name="New group"))

def test_modify_group_header(app):
    app.group.test_modify_first_group(Grupy(header="New header"))
