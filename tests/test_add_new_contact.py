from git.model.contact import ContactFormAttributes


def test_add_new_contact(fixt):
    old_contacts = fixt.contact.get_contact_list()
    contact = ContactFormAttributes(firstname="elena", middlename="test", lastname="lastname",
                                      nickname="nickname", title="QA", company="CPA", address="no address",
                                      mobile="+7 (495) 510-55-57", email="elena.dobranitsa@gmail.com", byear="1991",
                                      address2="no secondary address", phone2="Kiev", notes="no notes")
    fixt.contact.create(contact)
    assert len(old_contacts) + 1 == fixt.contact.count_contacts()
    new_contacts = fixt.contact.get_contact_list()

    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactFormAttributes.id_or_max) == sorted(new_contacts,
                                                                               key=ContactFormAttributes.id_or_max)
