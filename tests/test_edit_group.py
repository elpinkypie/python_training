from git.model.group import Group


def test_add_new_group(fixt):
    fixt.session.login(username="admin", password="secret")
    fixt.group.edit_first_group(Group(name="editgroup1", header="group2", footer="group3"))
    fixt.session.logout()

