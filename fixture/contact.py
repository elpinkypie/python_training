from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class ContactHelper:

    def __init__(self, fixt):
        self.fixt = fixt

    def fill_first_last_name(self, ct):
        wd = self.fixt.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(ct.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(ct.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(ct.lastname)

    def fill_nickname_title_company(self, ct):
        wd = self.fixt.wd
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(ct.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(ct.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(ct.company)

    def fill_address(self, ct):
        wd = self.fixt.wd
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(ct.address)

    def fill_home_work_phones(self, ct):
        wd = self.fixt.wd
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(ct.mobile)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(ct.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(ct.mobile)

    def fill_email(self, ct):
        wd = self.fixt.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(ct.email)

    def fill_birthday(self, ct):
        wd = self.fixt.wd
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("28")
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("August")
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(ct.byear)

    def button_enter_click(self):
        wd = self.fixt.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_phone2_notes(self, ct):
        wd = self.fixt.wd
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(ct.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(ct.notes)

    def fill_address2(self, ct):
        wd = self.fixt.wd
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(ct.address2)

    def fill_all_info(self, ct):
        self.fill_first_last_name(ct)
        self.fill_nickname_title_company(ct)
        self.fill_address(ct)
        self.fill_home_work_phones(ct)
        self.fill_email(ct)
        self.fill_birthday(ct)
        self.fill_address2(ct)
        self.fill_phone2_notes(ct)
        self.button_enter_click()

    def delete_first_contact(self):
        wd = self.fixt.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        #press delete
        wd.find_element_by_xpath('//div[@class="left"]/input[@value="Delete"]').click()
        wd.switch_to_alert().accept()
        # time.sleep(5)
        self.check_deletion_message()

    def edit_contact(self, ct):
        wd = self.fixt.wd
        #click edit contact
        wd.find_element_by_xpath('//a[@href="edit.php?id=7"]').click()
        self.fill_all_info(ct)
        wd.find_element_by_name("update").click()

    def modify_contact(self, ct):
        wd = self.fixt.wd
        # click modify contact
        wd.find_element_by_xpath('//a[@href="view.php?id=8"]').click()
        wd.find_element_by_name('modifiy').click()
        self.fill_all_info(ct)
        wd.find_element_by_name("update").click()

    def check_deletion_message(self):
        wd = self.fixt.wd
        element = wd.find_element_by_xpath('//*[@id="content"]/div[@class ="msgbox"]')
        WebDriverWait(wd, 6).until(EC.visibility_of_element_located('//*[@id="content"]/div[@class ="msgbox"]'))
        print(element)



