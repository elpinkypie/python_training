from git.model.group import Group
import pytest
from git.data.add_group import constant as test_data


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_new_group(fixt, group):
    old_groups = fixt.group.get_group_list()
    fixt.group.create(group)
    assert len(old_groups) + 1 == fixt.group.count()
    new_groups = fixt.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

