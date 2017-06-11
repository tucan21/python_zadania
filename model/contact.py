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
        self.home = homephone
        self.mobile = mobilephone
        self.work = workphone
        self.fax = fax
        self.email = email1
        self.email2 = email2
        self.address2 = address2
        self.phone2 = secondaryphone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
           return maxsize