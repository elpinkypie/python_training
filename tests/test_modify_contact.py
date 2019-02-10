from git.model.contact import ContactFormAttributes


def test_edit_contact(fixt):
    user_data = ContactFormAttributes(firstname="elenaeferf", middlename="testerfe", lastname="lastnameefe",
                                      nickname="nicknameef", title="QA", company="CPAerf", address="no address",
                                      mobile="+7 (495) 510-55-57", email="elena.dobranitsa22@gmail.com", byear="1993",
                                      address2="no secondary address", phone2="Kiev", notes="no notes")
    fixt.contact.modify_contact(user_data)
