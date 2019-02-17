from git.model.contact import ContactFormAttributes


def test_edit_contact(fixt):
    if fixt.contact.count_contacts() == 0:
        fixt.contact.create(ContactFormAttributes(firstname="firstname", lastname="lastname"))

    old_contacts = fixt.contact.get_contact_list()
    contact = ContactFormAttributes(firstname="edited", address="address", notes="notes")
    fixt.contact.edit_contact(contact)
    new_contacts = fixt.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)