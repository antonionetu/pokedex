from django.db import models

class Pokemon(models.Model):
    name = models.CharField(
        unique=True,
        max_length=255
    )

    views = models.IntegerField(
        default=0
    )