from git.model.group import Group


def test_edit_group(fixt):
    if fixt.group.count() == 0:
        fixt.group.create(Group(name="test"))

    fixt.group.edit_first_group(Group(name="editgroup1", header="group2", footer="group3"))

