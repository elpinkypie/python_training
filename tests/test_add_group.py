from git.model.group import Group


def test_add_new_group(fixt, data_groups):
    group = data_groups
    old_groups = fixt.group.get_group_list()
    fixt.group.create(group)
    assert len(old_groups) + 1 == fixt.group.count()
    new_groups = fixt.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

