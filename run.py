from lib.shopify import get_all_shopify_orders
from lib.certificate import Certificate
from lib.email import Email
from lib.s3 import s3_upload

if __name__ == '__main__':
    orders = get_all_shopify_orders()

    for order in orders:
        # TODO: use metadata instead of order note
        if order.note is not None and "Digital Email Delivered" in order.note:
            continue

        for line_item in order.line_items:
            if len(line_item.properties) == 0 or line_item.properties[0].name == "Donation":
                continue

            properties = dict([(p.name, p.value) for p in line_item.properties])
            if properties["E-mail"] == "NOGIFT" or properties["E-mail"] == "No Gift":
                properties["E-mail"] = order.email

            if properties["Name on the Certificate"] != '' and \
               properties['When do you want certificate sent'] != '':
                certificate = Certificate(line_item, properties)
                s3_upload(certificate)

                email = Email(certificate)
                if email.send():
                    # TODO: use metadata instead of order note
                    print("Updating order #{}".format(order.id))
                    if order.note is not None:
                        order.note = order.note + "\nDigital Email Delivered"
                    else:
                        order.note = "Digital Email Delivered"
                    order.save()