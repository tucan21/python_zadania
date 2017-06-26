from sys import maxsize

class Contact:

    def __init__(self, firstname= None, middlename= None, lastname= None, nickname= None, title= None, company= None,
                 address= None, homephone= None, mobilephone= None, workphone= None, fax= None, email1= None, email2= None,
                 address2= None, secondaryphone= None, id= None, all_phones_from_home_page= None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.firstname, self.lastname, self.middlename,
                                                                 self.nickname, self.title, self.company, self.address,
                                                                 self.homephone, self.mobilephone, self.workphone,
                                                                 self.fax, self.email1, self.email2, self.address2,
                                                                 self.secondaryphone)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
           return maxsize