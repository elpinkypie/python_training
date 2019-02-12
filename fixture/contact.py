from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ContactHelper:

    def __init__(self, fixt):
        self.fixt = fixt

    def change_field_value(self, field_name, text):
        wd = self.fixt.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

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
        self.change_field_value("home", ct.mobile)
        self.change_field_value("mobile", ct.mobile)
        self.change_field_value("work", ct.mobile)

    def fill_email(self, ct):
        self.change_field_value("email", ct.email)

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
        self.click_add_new_contact()
        self.fill_all_info(ct)
        self.button_enter_click()

    def check_success_message(self):
        wd = self.fixt.wd
        WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[@class ="msgbox"]')))

    def delete_first_contact(self):
        wd = self.fixt.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        #press delete
        wd.find_element_by_xpath('//div[@class="left"]/input[@value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.check_success_message()

    def edit_contact(self, ct):
        wd = self.fixt.wd
        #click edit contact
        wd.find_element_by_xpath('(//*[@id="maintable"]//img[@title="Edit"])[1]').click()
        self.fill_all_info(ct)
        self.click_button_update()
        self.check_success_message()

    def click_button_update(self):
        wd = self.fixt.wd
        wd.find_element_by_name("update").click()

    def modify_contact(self, ct):
        wd = self.fixt.wd
        # click modify contact
        wd.find_element_by_xpath('(//*[@id="maintable"]//img[@title="Details"])[1]').click()
        wd.find_element_by_name('modifiy').click()
        self.fill_all_info(ct)
        self.click_button_update()
        self.check_success_message()

    def count_contacts(self):
        wd = self.fixt.wd
        return len(wd.find_elements_by_name("selected[]"))

