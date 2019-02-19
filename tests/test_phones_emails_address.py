import re
from random import randrange


def test_contact_fields_on_home_page(fixt):
    index = randrange(len(fixt.contact.get_contact_list()))
    contact_from_home_page = fixt.contact.get_contact_list()[index]
    contact_from_edit_page = fixt.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_phones_on_view_page(fixt):
    contact_from_view_page = fixt.contact.get_contact_from_view_page(0)
    contact_from_edit_page = fixt.contact.get_contact_info_from_edit_page(0)
    assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)


def test_emails_on_view_page(fixt):
    emails_from_view_page = fixt.contact.get_contact_from_view_page(0)
    emails_from_edit_page = fixt.contact.get_contact_info_from_edit_page(0)
    assert merge_phones_like_on_home_page(emails_from_view_page) == merge_emails_like_on_home_page(emails_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.workphone, contact.mobilephone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))