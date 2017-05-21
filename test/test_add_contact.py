# -*- coding: utf-8 -*-
from model.kontakty import Kontakty

def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Kontakty(firstname="Jan", middlename="Krzysztof", lastname="Nowak", nickname="1111111", title="2222222", company="3333333", address="4444444", home="5555555",
                                      mobile="6666666", work="7777777", fax="8888888", email="qwertyu@02.pl", address2="9999999", phone2="0000000")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)