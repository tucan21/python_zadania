from model.contact import Contact


def test_modify_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="Ola", middlename="Katarzyna", lastname="Pawlak", nickname="12345678", title="987654321",
                                           company="CBO", address="Katowice", homephone="2233665544", mobilephone="6012345678",
                                           workphone="227895632", fax="224147856", email1="asdfgh@02.pl", email2="qazwsx@o2.pl",
                                           address2="asf@op.pl", secondaryphone="123023547"))
    contact = (Contact(firstname="Jan", middlename="Krzysztof", lastname="Pawlowski", nickname="1111111", title="2222222",
                       company="3333333", address="4444444", homephone="5555555", mobilephone="6666666", workphone="7777777", fax="8888888",
                       email1="qwertyu@02.pl", email2="zxcv@op.pl", address2="9999999", secondaryphone="0000000"))
    app.contact.edit_contact(contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact2(app,db, check_ui):
    old_contacts = db.get_contact_list()
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="Ola", middlename="Katarzyna", lastname="Pawlak", nickname="12345678", title="987654321",
                                           company="CBO", address="Katowice", homephone="2233665544", mobilephone="6012345678",
                                           workphone="227895632", fax="224147856", email1="asdfgh@02.pl", email2="qazwsx@o2.pl",
                                           address2="", secondaryphone=""))
    contact = (Contact(firstname="Jan", middlename="Krzysztof", lastname="Pawlowski", nickname="1111111", title="2222222",
                       company="3333333", address="4444444", homephone="5555555", mobilephone="6666666", workphone="7777777", fax="8888888",
                       email1="qwertyu@02.pl", email2="zxcv@op.pl", address2="9999999", secondaryphone="0000000"))
    old_contacts_ui = app.contact.get_contact_list()
    edited_contact = old_contacts_ui[0]
    app.contact.edit_contact(contact)
    new_contacts = db.get_contact_list()
    assert sorted([contact for contact in old_contacts if contact.id != edited_contact.id],
                  key=Contact.id_or_max) == sorted(
        [contact for contact in new_contacts if contact.id != edited_contact.id], key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
key=Contact.id_or_max)