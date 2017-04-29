from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sesie_kontakty import SessionHelperK
from fixture.grupy_K import GroupHelperK


class Aplikacja_kontakty:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelperK(self)
        self.group = GroupHelperK(self)


    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost:81/addressbook/")

    def destroy(self):
        self.wd.quit()