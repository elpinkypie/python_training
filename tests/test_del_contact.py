from git.model.contact import ContactFormAttributes


def test_delete_first_contact(fixt):
    if fixt.contact.count_contacts() == 0:
        fixt.contact.create(ContactFormAttributes(firstname="firstname", lastname="lastname"))
    fixt.contact.delete_first_contact()
