from git.model.group import Group


def test_modify_group_name(fixt):
    if fixt.group.count() == 0:
        fixt.group.create(Group(name="test"))
    old_groups = fixt.group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    fixt.group.modify_first_group(group)
    assert len(old_groups) == fixt.group.count()

    new_groups = fixt.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(fixt):
#     if fixt.group.count() == 0:
#         fixt.group.create(Group(name="test"))
#     old_groups = fixt.group.get_group_list()
#     fixt.group.modify_first_group(Group(header="New header"))
#     new_groups = fixt.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

