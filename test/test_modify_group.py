from model.group import Group

def test_modify_group_name(app, db, check_ui):
    old_groups = db.get_group_list()
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="warunki wstepne"))
    app.group.edit_group(Group(name="name1", header="header1", footer="footer1"))
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_name2(app, db, check_ui):
    old_groups = db.get_group_list()
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="warunki wstepne"))
    old_groups_ui = app.group.get_group_list()
    edited_group = old_groups_ui[0]
    new_group_value = Group(name="name1", header="header1", footer="footer1")
    app.group.edit_group(new_group_value)
    new_groups = db.get_group_list()
    assert sorted([group for group in new_groups if group.id != edited_group.id], key=Group.id_or_max) == sorted(
        [group for group in old_groups if group.id != edited_group.id], key=Group.id_or_max)
   # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)