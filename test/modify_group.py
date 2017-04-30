from model.grupy import Grupy


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.test_modify_first_group(Grupy("qqq", "qqq", "qqq"))
    app.session.logout()
    
