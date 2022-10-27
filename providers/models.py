from django.db import models
from work.models import Work
# Create your models here.


class Provider(models.Model):
    class Meta:
        verbose_name = '廠商'
        verbose_name_plural = '廠商'

    def __str__(self):
        return self.name

    name = models.CharField(
        verbose_name='廠商名稱', max_length=20, null=True, blank=False)
    address = models.CharField(
        verbose_name='地址', max_length=20, null=True, blank=False)
    tax_number = models.CharField(
        verbose_name='統編', max_length=20, null=True, blank=False)
    contact_person = models.CharField(
        verbose_name='聯絡人', max_length=20, null=True, blank=False)
    contact_number = models.CharField(
        verbose_name='聯絡電話', max_length=20, null=True, blank=False)


class ProviderWork(models.Model):
    class Meta:
        verbose_name = '廠商施作項目'
        verbose_name_plural = '廠商施作項目'

    def __str__(self):
        return f'{self.provider.name} - ${self.unit_price}'

    provider = models.ForeignKey(to=Provider, on_delete=models.CASCADE, null=True, blank=False, related_name='works', verbose_name='報價廠商')
    work = models.ForeignKey(to=Work, on_delete=models.CASCADE, null=False, blank=False, related_name='providers', verbose_name='施作項目')
    unit_price = models.PositiveSmallIntegerField(
        verbose_name='單價', null=True, blank=True, default=100)
    note = models.CharField(verbose_name='備註', max_length=100, null=True, blank=True)
    active = models.BooleanField('有效', null=False, blank=False, default=True)
