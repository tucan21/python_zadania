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

