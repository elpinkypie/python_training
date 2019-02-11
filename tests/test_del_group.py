from git.model.group import Group


def test_delete_first_group(fixt):
    if fixt.group.count() == 0:
        fixt.group.create(Group(name="test"))
    fixt.group.delete_first_group()
