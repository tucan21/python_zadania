# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Jan", middlename="Krzysztof", lastname="Nowak", nickname="1111111", title="2222222", company="3333333", address="4444444", homephone="5555555",
                      mobilephone="6666666", workphone="7777777", fax="8888888", email1="qwertyu@02.pl", email2="qazwsx@o2.pl",
                      address2="9999999", secondaryphone="0000000")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)