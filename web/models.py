from django.db import models

# Create your models here.


class BaseData(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    number = models.BigIntegerField(null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.name)