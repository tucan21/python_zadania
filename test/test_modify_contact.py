from model.contact import Contact
from random import randrange

#def test_modify_contact(app, db, check_ui):
#    old_contacts = db.get_contact_list()
#    if app.contact.count_contact() == 0:
#        app.contact.create_contact(Contact(firstname="Ola", middlename="Katarzyna", lastname="Pawlak", nickname="12345678",
#                    title="987654321",
#                    company="CBO", address="Katowice", homephone="2233665544", mobilephone="6012345678",
#                    workphone="227895632", fax="224147856", email1="asdfgh@02.pl", email2="qazwsx@o2.pl",
#                    address2="", secondaryphone=""))
#    new_contact_value = Contact(firstname="Jan", middlename="Krzysztof", lastname="Pawlowski", nickname="1111111", title="2222222",
#            company="3333333", address="4444444", homephone="5555555", mobilephone="6666666", workphone="7777777",
#            fax="8888888",
#            email1="qwertyu@02.pl", email2="zxcv@op.pl", address2="9999999", secondaryphone="0000000")
#    edited_contact_id = app.contact.edit_contact_and_get_id(new_contact_value)
#    new_contact_value.id = edited_contact_id
#    new_contacts = db.get_contact_list()
#    assert sorted([contact for contact in old_contacts if contact.id != edited_contact_id],key=Contact.id_or_max) == sorted([contact for contact in new_contacts if contact.id != edited_contact_id], key=Contact.id_or_max)
#    assert [contact for contact in new_contacts if contact.id == edited_contact_id] == [new_contact_value]
#    if check_ui:
#        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_modify_some_contact(app):
    if app.contact.count_contact() == 0:
        app.contact(Contact(firstname="Ola", middlename="Katarzyna", lastname="Pawlak", nickname="12345678", title="987654321",
                                           company="CBO", address="Katowice", homephone="2233665544", mobilephone="6012345678",
                                           workphone="227895632", fax="224147856", email1="asdfgh@02.pl", email2="qazwsx@o2.pl",
                                           address2="", secondaryphone=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Paulina", middlename="Magda-xxx", lastname="Kowalska--xxx", nickname="Paula--xxx", title="Mrs--xxx",
                                           company="DB--xxx", address="Krakow--xxx", homephone="2233665544--xxx", mobilephone="6012345678--xxx", workphone="227895632--xxx",
                                           fax="224147856--xxx", email1="asdfgh@02.pl--xxx", email2="sdf@op.pl--xxx", address2="--xxx", secondaryphone="-modyf")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
#    old_contacts[index] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)