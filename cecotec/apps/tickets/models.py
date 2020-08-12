from decimal import Decimal

from django.db import models
from django.db.models import Sum

from cecotec.apps.products.models import Product
from cecotec.apps.user.models import User
from cecotec.utils.models import TimeControl
from django.core.mail import send_mail

import csv
from io import StringIO
from django.core.mail import EmailMessage


# Create your models here.
class Ticket(TimeControl):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    def total(self):
        return f"{round(Decimal(self.productsinticket_set.all().aggregate(Sum('product__price'))['product__price__sum']), 2)}$"

    def save(self, *args, **kwargs):
        data = ProductsInTicket.objects.filter(ticket_id=self.id)
        csvfile = StringIO()
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(
            ['ticket_id', 'client_email', ])

        csvwriter.writerow(
            [data[0].ticket.id, data[0].ticket.client.email, ])

        csvwriter.writerow(['product_id', 'product_name', 'product_price'])

        for d in data:
            csvwriter.writerow(
                [d.product.id, d.product.name, f'{d.product.price}$', ])

        csvwriter.writerow(['total:', f'{self.total()}'])

        email = EmailMessage(
            f'{self.client.email} has made a new purchase!',
            f'{self.client.email} has purchased a total of {self.total()}',
            'jeronimobarealucas@gmail.com',
            ['jeronimobarealucas@gmail.com'],
        )
        email.attach('ticket.csv', csvfile.getvalue(), 'text/csv')
        email.send()

        super().save(*args, **kwargs)


class ProductsInTicket(TimeControl):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
