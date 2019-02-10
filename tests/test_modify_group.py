from git.model.group import Group




def test_modify_group_name(fixt):
    fixt.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(fixt):
    fixt.group.modify_first_group(Group(header="New header"))
