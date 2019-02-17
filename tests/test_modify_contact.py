from git.model.contact import ContactFormAttributes
from random import randrange


def test_modify_contact(fixt):
    if fixt.contact.count_contacts() == 0:
        fixt.contact.create(ContactFormAttributes(firstname="firstname", lastname="lastname"))
    old_contacts = fixt.contact.get_contact_list()

    # random choose contact
    index = randrange(len(old_contacts))
    contact = ContactFormAttributes(firstname="modified")
    contact.id = old_contacts[index].id
    fixt.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == fixt.contact.count_contacts()

    new_contacts = fixt.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactFormAttributes.id_or_max) == sorted(new_contacts,
                                                                               key=ContactFormAttributes.id_or_max)
