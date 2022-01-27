import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from shopify import line_item

### Sends a test email from SES

def get_env_data_as_dict(path: str) -> dict:
    with open(path, 'r') as f:
       return dict(tuple(line.replace('\n', '').split('=')) for line
                in f.readlines() if not line.startswith('#'))

os.environ.update(get_env_data_as_dict('.env'))

from lib.certificate import Certificate
from lib.email import Email


# Generate test certificate

attributes = dict()
# This is actually the whale's name!
attributes["title"] = "Salt"
lineitem = line_item.LineItem(attributes, {})

properties = dict()
# Make sure you include letters with descenders!
properties["Name on the Certificate"] = "Testing 123 Query"
properties["Message"] = "We sincerely hope you enjoy your whale!"
# Make first arg in practice
properties["E-mail"] = "mark@mrh.io"
# %m/%d/%Y"
properties["When do you want certificate sent"] = "12/12/2012"

certificate = Certificate(lineitem, properties)
email = Email(certificate)

email.send()