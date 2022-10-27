from pyexpat import model
from django.db import models

# Create your models here.

class QuotationSettings(models.Model):
    def __str__(self):
        return f'{self.name}'
    
    default_weighting = models.FloatField(verbose_name='預設乘數', null=True, default=1.2)