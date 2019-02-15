from git.model.group import Group


def test_modify_group_name(fixt):
    if fixt.group.count() == 0:
        fixt.group.create(Group(name="test"))
    old_groups = fixt.group.get_group_list()
    fixt.group.modify_first_group(Group(name="New group"))
    new_groups = fixt.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(fixt):
    if fixt.group.count() == 0:
        fixt.group.create(Group(name="test"))
    old_groups = fixt.group.get_group_list()
    fixt.group.modify_first_group(Group(header="New header"))
    new_groups = fixt.group.get_group_list()
    assert len(old_groups) == len(new_groups)

