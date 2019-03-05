from django.utils import timezone
from django.db.models import CharField, TextField, DateTimeField
from django.db import models as models

# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.nama

