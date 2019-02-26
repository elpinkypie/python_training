from git.model.contact import ContactFormAttributes
import random
import string
import os.path
import jsonpickle
import sys
import getopt


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [ContactFormAttributes(firstname="", middlename="", homephone="", byear="1991")] + [
    ContactFormAttributes(firstname=random_string(10), middlename=random_string(10), lastname=random_string(10),
                          homephone=random_string(10), email1=random_string(10), byear="1991", notes=random_string(10))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))