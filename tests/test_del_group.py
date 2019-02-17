from git.model.group import Group
from random import randrange

def test_delete_first_group(fixt):
    if fixt.group.count() == 0:
        fixt.group.create(Group(name="test"))
    old_groups = fixt.group.get_group_list()

    #random index to choose random group
    index = randrange(len(old_groups))
    fixt.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == fixt.group.count()

    new_groups = fixt.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups
