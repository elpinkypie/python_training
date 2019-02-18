from sys import maxsize


class ContactFormAttributes:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, workphone=None, mobilephone=None, email=None,
                 byear=None, phone2=None, notes=None, address2=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.email = email
        self.byear = byear
        self.phone2 = phone2
        self.notes = notes
        self.address2 = address2
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
                and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
                and (self.lastname is None or other.firstname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize