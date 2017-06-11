# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " *10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("firstname", 5), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), title=random_string("nickname", 10), company=random_string("company", 10),
            address=random_string("address", 10), homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10),
            workphone=random_string("workphone", 10), fax=random_string("fax", 10), email1=random_string("email1", 10),
            email2=random_string("email2", 10), address2=random_string("address2", 10), secondaryphone=random_string("secondaryphone", 10))
    for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    #old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)
