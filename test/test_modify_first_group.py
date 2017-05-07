from model.grupy import Grupy

def test_modify_first_group(app):
    if app.group.count_group() == 0:
        app.group.create_group(Grupy(name="test"))
    app.group.edit_group(Grupy("qqq", "qqq", "qqq"))

def test_modify_group_name(app):
    if app.group.count_group() == 0:
        app.group.create_group(Grupy(name="warunki wstepne"))
    app.group.edit_group(Grupy(name="New group"))

def test_modify_group_header(app):
    if app.group.count_group() == 0:
        app.group.create_group(Grupy(header="warunki wstepne"))
    app.group.edit_group(Grupy(header="New header"))

