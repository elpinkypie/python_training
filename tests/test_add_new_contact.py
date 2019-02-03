from git.model.contact import ContactFormAttributes


def test_add_new_contact(fixt):
    fixt.session.login(username="admin", password="secret")
    user_data = ContactFormAttributes(firstname="elena", middlename="test", lastname="lastname",
                                      nickname="nickname", title="QA", company="CPA", address="no address",
                                      mobile="+7 (495) 510-55-57", email="elena.dobranitsa@gmail.com", byear="1991",
                                      address2="no secondary address", phone2="Kiev", notes="no notes")
    fixt.contact.fill_first_last_name(user_data)
    fixt.contact.fill_nickname_title_company(user_data)
    fixt.contact.fill_address(user_data)
    fixt.contact.fill_home_work_phones(user_data)
    fixt.contact.fill_email(user_data)
    fixt.contact.fill_birthday(user_data)
    fixt.contact.fill_address2(user_data)
    fixt.contact.fill_phone2_notes(user_data)
    fixt.contact.button_enter_click()
    fixt.session.logout()
