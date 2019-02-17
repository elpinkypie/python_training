from git.model.contact import ContactFormAttributes
from random import randrange


def test_delete_first_contact(fixt):
    if fixt.contact.count_contacts() == 0:
        fixt.contact.create(ContactFormAttributes(firstname="firstname", lastname="lastname"))
    old_contacts = fixt.contact.get_contact_list()

    #random choose contact
    index = randrange(len(old_contacts))
    fixt.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == fixt.contact.count_contacts()

    new_contacts = fixt.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
