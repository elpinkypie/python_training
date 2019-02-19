from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from git.model.contact import ContactFormAttributes
import re

class ContactHelper:

    def __init__(self, fixt):
        self.fixt = fixt

    def change_field_value(self, field_name, text):
        wd = self.fixt.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_home_page(self):
        wd = self.fixt.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_class_name('fdTableSortTrigger')) > 0):
            wd.find_element_by_link_text("home").click()

    def click_add_new_contact(self):
        wd = self.fixt.wd
        wd.find_element_by_xpath('//*[@id="nav"]//a[@href="edit.php"]').click()

    def fill_first_last_name(self, ct):
        self.change_field_value("firstname", ct.firstname)
        self.change_field_value("middlename", ct.middlename)
        self.change_field_value("lastname", ct.lastname)

    def fill_nickname_title_company(self, ct):
        self.change_field_value("nickname", ct.nickname)
        self.change_field_value("title", ct.title)
        self.change_field_value("company", ct.company)

    def fill_address(self, ct):
        self.change_field_value("address", ct.address)

    def fill_home_work_phones(self, ct):
        self.change_field_value("home", ct.homephone)
        self.change_field_value("mobile", ct.mobilephone)
        self.change_field_value("work", ct.workphone)

    def fill_email(self, ct):
        self.change_field_value("email1", ct.email1)
        self.change_field_value("email2", ct.email2)
        self.change_field_value("email3", ct.email3)

    def fill_birthday(self, ct):
        wd = self.fixt.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("28")
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
        self.change_field_value("byear", ct.byear)

    def button_enter_click(self):
        wd = self.fixt.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_phone2_notes(self, ct):
        self.change_field_value("phone2", ct.phone2)
        self.change_field_value("notes", ct.notes)

    def fill_address2(self, ct):
        self.change_field_value("address2", ct.address2)

    def fill_all_info(self, ct):
        self.fill_first_last_name(ct)
        self.fill_nickname_title_company(ct)
        self.fill_address(ct)
        self.fill_home_work_phones(ct)
        self.fill_email(ct)
        self.fill_birthday(ct)
        self.fill_address2(ct)
        self.fill_phone2_notes(ct)

    def create(self, ct):
        self.open_home_page()
        self.click_add_new_contact()
        self.fill_all_info(ct)
        self.button_enter_click()
        self.contact_cache = None

    def check_success_message(self):
        wd = self.fixt.wd
        WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[@class ="msgbox"]')))

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.fixt.wd
        self.open_home_page()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        #press delete
        wd.find_element_by_xpath('//div[@class="left"]/input[@value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.check_success_message()
        self.contact_cache = None

    def edit_first_contact(self, ct):
        self.edit_contact_by_index(0, ct)

    def edit_contact_by_index(self, index, ct):
        wd = self.fixt.wd
        self.open_home_page()
        #click edit contact
        wd.find_elements_by_xpath('//*[@id="maintable"]//img[@title="Edit"]')[index].click()
        self.fill_all_info(ct)
        self.click_button_update()
        self.check_success_message()
        self.contact_cache = None

    def click_button_update(self):
        wd = self.fixt.wd
        wd.find_element_by_name("update").click()

    def modify_first_contact(self, ct):
        self.modify_contact_by_index(0, ct)

    def modify_contact_by_index(self, index, ct):
        wd = self.fixt.wd
        self.open_home_page()
        # click modify contact
        wd.find_elements_by_xpath('//*[@id="maintable"]//img[@title="Details"]')[index].click()
        wd.find_element_by_name('modifiy').click()
        self.fill_all_info(ct)
        self.click_button_update()
        self.check_success_message()
        self.contact_cache = None

    def count_contacts(self):
        wd = self.fixt.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.fixt.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                #lastname
                text = cells[1].text
                #firstname
                text2 = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(ContactFormAttributes(firstname=text2, lastname=text, id=id, address=address,
                                                                all_phones_from_home_page=all_phones,
                                                                all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.fixt.wd
        self.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.fixt.wd
        self.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.fixt.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")

        return ContactFormAttributes(firstname=firstname, lastname=lastname, id=id,
                                     homephone=homephone, workphone=workphone, mobilephone=mobilephone, phone2=phone2,
                                     email1=email1, email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.fixt.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)

        return ContactFormAttributes(homephone=homephone, workphone=workphone, mobilephone=mobilephone, phone2=phone2)