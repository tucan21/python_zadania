from model.grupy import Grupy

def test_delete_first_group(app):
    if app.group.count_group() == 0:
        app.group.create_group(Grupy(name="test"))
    app.group.del_group()
