from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Pages(models.Model):
    name = models.TextField()
    page = models.TextField()

class Barrapunto(models.Model):
    title = models.TextField()
    link = models.TextField()
