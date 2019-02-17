from git.model.contact import ContactFormAttributes


def test_delete_first_contact(fixt):
    if fixt.contact.count_contacts() == 0:
        fixt.contact.create(ContactFormAttributes(firstname="firstname", lastname="lastname"))
    old_contacts = fixt.contact.get_contact_list()
    fixt.contact.delete_first_contact()
    assert len(old_contacts) - 1 == fixt.contact.count_contacts()

    new_contacts = fixt.contact.get_contact_list()
    old_contacts[0:1] = []
    print(old_contacts)
    assert old_contacts == new_contacts
