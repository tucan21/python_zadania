# -*- coding: utf-8 -*-
from model.contact import Contact

#def test_add_new_contact(app, db, json_contacts, check_ui):
#    contact = json_contacts
#    old_contacts = db.get_contact_list()
#    app.contact.create_contact(contact)
#    new_contacts = db.get_contact_list()
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#    if check_ui:
#        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
#                                                                     key=Contact.id_or_max)

def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ola", middlename="Katarzyna", lastname="Pawlak", nickname="12345678", title="987654321",
                                           company="CBO", address="Katowice", homephone="2233665544", mobilephone="6012345678",
                                           workphone="227895632", fax="224147856", email1="asdfgh@02.pl", email2="qazwsx@o2.pl",
                                           address2="", secondaryphone="")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    sorted(old_contacts + [contact], key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
