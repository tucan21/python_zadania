# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app, json_contacts):
    print(json_contacts)
    contact = json_contacts
    #old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    #assert len(old_contacts) + 1 == app.count_contact()
    #new_contacts = app.contact.get_contact_list()
    #old_contacts.append(contact)
    #assert len(old_contacts) + 1 == len(new_contacts)
