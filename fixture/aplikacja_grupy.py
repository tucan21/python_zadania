from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sesje_grupy import SessionHelperG


class Aplikacja_grupy:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelperG(self)


    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def fill_form(self, grupy):
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(grupy.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(grupy.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(grupy.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()


    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost:81/addressbook/")

    def destroy(self):
        self.wd.quit()