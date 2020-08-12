from django.db import models
from cecotec.utils.models import TimeControl


# Create your models here.
class Product(TimeControl):
    name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}$'
