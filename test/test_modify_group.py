from model.group import Group
from random import randrange

#def test_modify_first_group(app):
#    if app.group.count_group() == 0:
#       app.group.create_group(Grupy(name="test"))
#   old_groups = app.group.get_group_list()
#   app.group.edit_group(Grupy("qqq", "qqq", "qqq"))
#   new_groups = app.group.get_group_list()
#   assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="warunki wstepne"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
#    if app.group.count_group() == 0:
#        app.group.create_group(Grupy(header="warunki wstepne"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_group(Grupy(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

