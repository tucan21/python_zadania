from sys import maxsize

class Kontakty:

    def __init__(self, firstname= None, middlename= None, lastname= None, nickname= None, title= None, company= None,
                 address= None, home= None, mobile= None, work= None, fax= None, email= None, address2= None, phone2= None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.address2 = address2
        self.phone2 = phone2

    def __repr__(self):
        return "%s:%s" % (self.firstname, self.lastname)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
