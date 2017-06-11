from model.contact import Contact

def test_modify_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(firstname="Ola", middlename="Katarzyna", lastname="Pawlak", nickname="12345678", title="987654321",
                                           company="CBO", address="Katowice", homephone="2233665544", mobilephone="6012345678",
                                           workphone="227895632", fax="224147856", email1="asdfgh@02.pl", email2="qazwsx@o2.pl",
                                           address2="", secondaryphone=""))
    contact = (Contact(firstname="Jan", middlename="Krzysztof", lastname="Pawlowski", nickname="1111111", title="2222222",
                       company="3333333", address="4444444", homephone="5555555", mobilephone="6666666", workphone="7777777", fax="8888888",
                       email1="qwertyu@02.pl", email2="zxcv@op.pl", address2="9999999", secondaryphone="0000000"))
#    contact.id = old_contacts[0].id
    app.contact.edit_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0] = contact
#   assert sorted(old_contacts, key=Kontakty.id_or_max) == sorted(new_contacts, key=Kontakty.id_or_max)
