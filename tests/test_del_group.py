

def test_delete_first_group(fixt):
    fixt.session.login(username="admin", password="secret")
    fixt.group.delete_first_group()
    fixt.session.logout()
