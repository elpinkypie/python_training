from git.model.contact import ContactFormAttributes


def test_add_new_contact(fixt, json_contacts):
    contact = json_contacts
    old_contacts = fixt.contact.get_contact_list()
    fixt.contact.create(contact)
    assert len(old_contacts) + 1 == fixt.contact.count_contacts()
    new_contacts = fixt.contact.get_contact_list()

    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactFormAttributes.id_or_max) == sorted(new_contacts,
                                                                               key=ContactFormAttributes.id_or_max)
