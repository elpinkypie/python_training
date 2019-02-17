from git.model.group import Group

def test_add_new_group(fixt):
    old_groups = fixt.group.get_group_list()
    group = Group(name="gergerg", header="scsdcvs", footer="vsdvsv")
    fixt.group.create(group)
    new_groups = fixt.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(fixt):
    old_groups = fixt.group.get_group_list()
    group = Group(name="", header="", footer="")
    fixt.group.create(group)
    new_groups = fixt.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
