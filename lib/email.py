import os
from datetime import datetime

import boto3

fb_pages = dict()
fb_pages['Bayou'] = 'https://www.facebook.com/Bayou-The-Whale-613697128802762/'
fb_pages['Cajun'] = 'https://www.facebook.com/Cajun-The-Whale-1071772439577595/'
fb_pages['Etch-a-Sketch'] = 'https://www.facebook.com/Etch-A-Sketch-the-Whale-1665318120352607/'
fb_pages['Owl'] = 'https://www.facebook.com/owlthewhale/'
fb_pages['Salt'] = 'https://www.facebook.com/saltthewhale/'

ses = boto3.client(
    'ses',
    region_name=os.getenv("REGION_NAME"),
    aws_access_key_id=os.getenv('SES_AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('SES_AWS_SECRET_ACCESS_KEY')
)


class Email(object):
    txt_email_path = os.path.dirname(os.path.realpath(__file__)) + "/../templates/email.txt"
    html_email_path = os.path.dirname(os.path.realpath(__file__)) + "/../templates/email.html"

    def __init__(self, certificate):
        super(Email, self).__init__()
        self.email = certificate.email
        self.file_name = certificate.local_path.replace("/tmp/", "")
        self.user_name = certificate.name_on_certificate
        self.whale_name = certificate.whale_name
        self.gift_message_email = certificate.message
        self.facebook_page = fb_pages[certificate.whale_name]
        self.when = certificate.when

    def send(self):
        # send the e-mail both to the adopter and the user if it has any
        if self.when > datetime.today():
            return False

        to_addresses = ["adoptions@whale.org", "henderson.mark@gmail.com"]
        new_addresses = self.email.split(',')

        response = ses.send_email(
            Source='adoptions@whale.org',
            Destination={
                'ToAddresses': to_addresses + new_addresses
            },
            Message={
                'Subject': {
                    'Data': 'Your Whale Adoption Package is Ready!',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': open(self.txt_email_path, "r").read().format(
                            self.file_name),
                        'Charset': 'UTF-8'
                    },
                    'Html': {
                        'Data': open(self.html_email_path, "r").read().format(
                                self.user_name,
                                self.whale_name,
                                self.file_name,
                            ),
                        'Charset': 'UTF-8'
                    }
                }
            }
        )

        print(response)

        return True
