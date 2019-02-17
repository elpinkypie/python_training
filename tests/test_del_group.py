from git.model.group import Group


def test_delete_first_group(fixt):
    if fixt.group.count() == 0:
        fixt.group.create(Group(name="test"))
    old_groups = fixt.group.get_group_list()
    fixt.group.delete_first_group()
    new_groups = fixt.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
