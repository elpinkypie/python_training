from git.model.contact import ContactFormAttributes


def test_add_new_contact(fixt):

    fixt.contact.create(ContactFormAttributes(firstname="elena", middlename="test", lastname="lastname",
                                      nickname="nickname", title="QA", company="CPA", address="no address",
                                      mobile="+7 (495) 510-55-57", email="elena.dobranitsa@gmail.com", byear="1991",
                                      address2="no secondary address", phone2="Kiev", notes="no notes"))
