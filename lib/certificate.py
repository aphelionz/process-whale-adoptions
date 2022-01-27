from datetime import datetime
import os

from PIL import Image, ImageFont, ImageDraw
import shopify


class Certificate(object):
    templates_path = os.path.dirname(os.path.realpath(__file__)) + "/../templates"
    fonts_path = os.path.dirname(os.path.realpath(__file__)) + "/../fonts"

    def __init__(self, line_item: shopify.line_item.LineItem, properties: dict) -> None:
        super(Certificate, self).__init__()

        self.whale_name = line_item.title
        self.name_on_certificate = properties['Name on the Certificate']
        self.message = properties["Message"]
        self.email = properties["E-mail"]
        self.when = properties.get('When do you want certificate sent',
                                   datetime.today().strftime("%m/%d/%Y"))
        self.when = datetime.strptime(self.when, "%m/%d/%Y")

        self.draw_certificate(properties['Name on the Certificate'], line_item.title)

    def draw_certificate(self, name_on_certificate, whale_name):
        img = Image.open("{}/{}_cert_new_template.jpg".format(
            self.templates_path,
            whale_name.lower()))
        draw = ImageDraw.Draw(img)
        w, h = draw.textsize(name_on_certificate)
        start_draw_point = 2140
        start_vertical_point = 1870
        chars = set('gjpqy')  # characters with descenders
        if any((c in chars) for c in name_on_certificate):
            start_vertical_point = 1860
        if w <= 222:
            divide_name = w/2
            start_draw_point = start_draw_point + (111-divide_name)*7.25
        font = ImageFont.truetype(self.fonts_path + '/Merriweather-Bold.ttf', 80)
        draw.text(
            (start_draw_point, start_vertical_point),
            name_on_certificate,
            (0, 0, 0),
            font=font)
        self.local_path = '/tmp/{}_certificate_{}.jpg'.format(name_on_certificate, whale_name)
        img.save(self.local_path, quality=100)
        print("Certificate successfully saved to", self.local_path)
