from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.contact import ContactHelper


class Aplication:
    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost:81/addressbook/")

    def destroy(self):
        self.wd.quit()
