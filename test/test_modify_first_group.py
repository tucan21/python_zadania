from model.grupy import Grupy

#def test_modify_first_group(app):
#    if app.group.count_group() == 0:
#       app.group.create_group(Grupy(name="test"))
#   old_groups = app.group.get_group_list()
#   app.group.edit_group(Grupy("qqq", "qqq", "qqq"))
#   new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    if app.group.count_group() == 0:
       app.group.create_group(Grupy(name="warunki wstepne"))
    old_groups = app.group.get_group_list()
    group = Grupy(name="New group")
    group.id = old_groups[0].id
    app.group.edit_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Grupy.id_or_max) == sorted(new_groups, key=Grupy.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count_group() == 0:
#        app.group.create_group(Grupy(header="warunki wstepne"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_group(Grupy(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

