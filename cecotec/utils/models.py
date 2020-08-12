from django.db import models


class TimeControl(models.Model):
    created_at = models.DateTimeField(
        auto_now=True,
    )
    last_modification = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        abstract = True
