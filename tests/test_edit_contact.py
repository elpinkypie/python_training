from git.model.contact import ContactFormAttributes


def test_edit_contact(fixt):
    if fixt.contact.count_contacts() == 0:
        fixt.contact.create(ContactFormAttributes(firstname="firstname", lastname="lastname"))

    fixt.contact.edit_contact(ContactFormAttributes(firstname="edited", address="address", notes="notes"))
