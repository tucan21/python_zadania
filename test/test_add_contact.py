# -*- coding: utf-8 -*-
from model.kontakty import Kontakty

def test_add_new_contact(app):
    app.group.create_contact(Kontakty(firstname="Jan", middlename="Krzysztof", lastname="Nowak", nickname="1111111", title="2222222", company="3333333", address="4444444", home="5555555",
                                      mobile="6666666", work="7777777", fax="8888888", email="qwertyu@02.pl", address2="9999999", phone2="0000000"))