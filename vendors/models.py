from django.db import models

class Vendor(models.Model):
    class Meta:
        verbose_name = '廠商'
        verbose_name_plural = '廠商'

    def __str__(self):
        return self.name

    name = models.CharField(
        verbose_name='廠商名稱', max_length=20, null=True, blank=False)
    contact_person = models.CharField(
        verbose_name='聯絡人', max_length=20, null=True, blank=True)
    contact_number = models.CharField(
        verbose_name='聯絡電話', max_length=20, null=True, blank=True)
    address = models.CharField(
        verbose_name='地址', max_length=20, null=True, blank=True)
    tax_number = models.CharField(
        verbose_name='統編', max_length=20, null=True, blank=True)
