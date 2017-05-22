from model.grupy import Grupy

class GroupHelper:
    def __init__(self, app):
        self.app = app


    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create_group(self, grupy):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(grupy)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_form(self, grupy):
        wd = self.app.wd
        self.chng_field_value("group_name", grupy.name)
        self.chng_field_value("group_header", grupy.header)
        self.chng_field_value("group_footer", grupy.footer)

    def chng_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_group(self):
        self.del_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def del_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_group(self):
        self.edit_group_by_index(0)

    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()


    def count_group(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Grupy(name=text, id=id))
        return list(self.group_cache)
