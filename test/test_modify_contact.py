from model.kontakty import Kontakty

def test_modify_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Kontakty(firstname="Ola", middlename="Katarzyna", lastname="Pawlak", nickname="12345678", title="987654321",
                                            company="CBO", address="Katowice", home="2233665544", mobile="6012345678", work="227895632",
                                            fax="224147856", email="asdfgh@02.pl", address2="", phone2=""))
    app.contact.edit_contact(Kontakty(firstname="Jan", middlename="Krzysztof", lastname="Nowakowski", nickname="1111111", title="2222222",
                                      company="3333333", address="4444444", home="5555555", mobile="6666666", work="7777777", fax="8888888",
                                      email="qwertyu@02.pl", address2="9999999", phone2="0000000"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)