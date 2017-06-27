from model.group import Group

def test_modify_group_name2(app, db, check_ui):
    old_groups = db.get_group_list()
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="warunki wstepne"))
    old_groups_ui = app.group.get_group_list()
    edited_group_id = old_groups_ui[0].id
    new_group_value = Group(name="name1", header="header1", footer="footer1", id=edited_group_id)
    app.group.edit_group(new_group_value)
    new_groups = db.get_group_list()
    assert sorted([group for group in new_groups if group.id != edited_group_id], key=Group.id_or_max) == sorted([group for group in old_groups if group.id != edited_group_id], key=Group.id_or_max)
    assert [group for group in new_groups if group.id == edited_group_id] == [new_group_value]
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)