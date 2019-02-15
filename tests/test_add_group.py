from git.model.group import Group


def test_add_new_group(fixt):
    old_groups = fixt.group.get_group_list()
    fixt.group.create(Group(name="gergerg", header="scsdcvs", footer="vsdvsv"))
    new_groups = fixt.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(fixt):
    old_groups = fixt.group.get_group_list()
    fixt.group.create(Group(name="", header="", footer=""))
    new_groups = fixt.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
