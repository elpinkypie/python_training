class SessionHelper:

    def __init__(self, fixt):
        self.fixt = fixt

    def login(self, username, password):
        wd = self.fixt.wd
        self.fixt.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.implicitly_wait(30)

    def logout(self):
        wd = self.fixt.wd
        wd.find_element_by_link_text("Logout").click()
