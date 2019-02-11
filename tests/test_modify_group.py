from git.model.group import Group


def test_modify_group_name(fixt):
    if fixt.group.count() == 0:
        fixt.group.create(Group(name="test"))
    fixt.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(fixt):
    if fixt.group.count() == 0:
        fixt.group.create(Group(name="test"))
    fixt.group.modify_first_group(Group(header="New header"))
