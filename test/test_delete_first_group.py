from model.grupy import Grupy

def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count_group() == 0:
        app.group.create_group(Grupy(name="test"))
    app.group.del_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups