# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from group import ContactFormAttributes

class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        # self.verificationErrors = []
        # self.accept_next_alert = True

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def fill_first_last_name(self, wd, ct):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(ct.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(ct.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(ct.lastname)

    def fill_nickname_title_company(self, wd, ct):
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(ct.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(ct.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(ct.company)

    def fill_address(self, wd, ct):
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(ct.address)

    def fill_home_work_phones(self, wd, ct):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(ct.mobile)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(ct.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(ct.mobile)

    def fill_email(self, wd, ct):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(ct.email)

    def fill_birthday(self, wd, ct):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("28")
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(ct.byear)

    def button_enter_click(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_phone2_notes(self, wd, ct):
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(ct.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(ct.notes)

    def fill_address2(self, wd, ct):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(ct.address)


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.fill_first_last_name(wd, ContactFormAttributes(firstname="elena", middlename="test", lastname="lastname"))
        self.fill_nickname_title_company(wd, ContactFormAttributes(nickname="nickname", title="QA", company="CPA"))

        self.fill_address(wd, ContactFormAttributes(address="no address"))
        self.fill_home_work_phones(wd, ContactFormAttributes(mobile="+7 (495) 510-55-57"))

        self.fill_email(wd, ContactFormAttributes(email="elena.dobranitsa@gmail.com"))

        self.fill_birthday(wd, ContactFormAttributes(byear="1991"))

        self.fill_address2(wd, ContactFormAttributes(address="no secondary address"))

        self.fill_phone2_notes(wd, ContactFormAttributes(phone2="Kiev", notes="no notes"))
        self.button_enter_click(wd)
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
