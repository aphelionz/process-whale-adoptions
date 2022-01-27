import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

### Generates a test certificate

from lib.certificate import Certificate
from shopify import line_item

attributes = dict()
# This is actually the whale's name!
attributes["title"] = "Salt"
lineitem = line_item.LineItem(attributes, {})

properties = dict()
# Make sure you include letters with descenders!
properties["Name on the Certificate"] = "Testing 123 Query"
properties["Message"] = "We sincerely hope you enjoy your whale!"
properties["E-mail"] = "testing@123.com"
# %m/%d/%Y"
properties["When do you want certificate sent"] = "12/12/2012"

Certificate(lineitem, properties)