from git.model.group import Group


def test_add_new_group(fixt):
    fixt.group.create(Group(name="gergerg", header="scsdcvs", footer="vsdvsv"))


def test_add_empty_group(fixt):
    fixt.group.create(Group(name="", header="", footer=""))

