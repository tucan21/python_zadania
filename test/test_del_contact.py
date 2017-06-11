from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="Ola", middlename="Katarzyna", lastname="Pawlak", nickname="12345678", title="987654321",
                                           company="CBO", address="Katowice", homephone="2233665544", mobilephone="6012345678", workphone="227895632",
                                           fax="224147856", email1="asdfgh@02.pl", email2="sdf@op.pl", address2="", secondaryphone=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.del_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
