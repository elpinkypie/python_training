from git.model.contact import ContactFormAttributes


def test_modify_contact(fixt):
    if fixt.contact.count_contacts() == 0:
        fixt.contact.create(ContactFormAttributes(firstname="firstname", lastname="lastname"))

    old_contacts = fixt.contact.get_contact_list()
    contact = ContactFormAttributes(firstname="modified")
    contact.id = old_contacts[0].id
    fixt.contact.modify_contact(contact)
    new_contacts = fixt.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactFormAttributes.id_or_max) == sorted(new_contacts,
                                                                               key=ContactFormAttributes.id_or_max)
