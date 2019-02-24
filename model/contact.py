from sys import maxsize


class ContactFormAttributes:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, workphone=None, mobilephone=None, email1=None, email2=None, email3=None,
                 byear=None, phone2=None, notes=None, address2=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
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
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.byear = byear
        self.phone2 = phone2
        self.notes = notes
        self.address2 = address2
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.homephone, self.email1)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
                and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
                and (self.lastname is None or other.firstname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize