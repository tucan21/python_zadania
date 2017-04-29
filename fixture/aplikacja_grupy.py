from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sesje_grupy import SessionHelperG
from fixture.grupy import GroupHelperG


class Aplikacja_grupy:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelperG(self)
        self.group = GroupHelperG(self)


    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost:81/addressbook/")

    def destroy(self):
        self.wd.quit()