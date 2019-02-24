from git.model.contact import ContactFormAttributes
import pytest
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [ContactFormAttributes(firstname="", middlename="", homephone="", byear="1991")] + [
    ContactFormAttributes(firstname=random_string(10), middlename=random_string(10), lastname=random_string(10),
                          homephone=random_string(10), email1=random_string(10), byear="1991", notes=random_string(10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_new_contact(fixt, contact):
    old_contacts = fixt.contact.get_contact_list()
    fixt.contact.create(contact)
    assert len(old_contacts) + 1 == fixt.contact.count_contacts()
    new_contacts = fixt.contact.get_contact_list()

    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactFormAttributes.id_or_max) == sorted(new_contacts,
                                                                               key=ContactFormAttributes.id_or_max)


 # contact = ContactFormAttributes(firstname="elena", middlename="test", lastname="lastname",
 #                                    nickname="nickname", title="QA", company="CPA", address="no address",
 #                                    homephone="+7 (495) 510-55-55", workphone="+7 (495) 510-55-56",
 #                                    mobilephone="+7 (495) 510-55-57",
 #                                    email1="elena.dobranitsa@gmail.com", byear="1991",
 #                                    address2="no secondary address", phone2="Kiev", notes="no notes")