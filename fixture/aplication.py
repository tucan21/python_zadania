from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Aplikacja:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

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
