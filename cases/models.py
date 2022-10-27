from tkinter import CASCADE
from django.db import models
from space_settings.models import SpaceName
# Create your models here.

class Customer(models.Model):
    class Meta:
        verbose_name = '業主'
        verbose_name_plural = '業主'

    def __str__(self):
        return self.name
        
    name = models.CharField(
        verbose_name='業主', max_length=20, null=True, blank=False)
    contact_number = models.CharField(verbose_name='聯絡方式', max_length=20, null=True, blank=True)


class Case(models.Model):
    class Meta:
        verbose_name = '案件'
        verbose_name_plural = '案件'

    def __str__(self):
        return f'{self.case_number} {self.name}'
        
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, null=True, blank=True, verbose_name='客戶')
    case_number = models.CharField(verbose_name='案號', max_length=30, null=True, blank=False)
    name = models.CharField(verbose_name='案名', max_length=20, null=True, blank=False)
    address = models.CharField(verbose_name='地址', max_length=50, null=True, blank=True)
    total_area = models.FloatField(verbose_name='總坪數', null=True, blank=True)


class CaseSpace(models.Model):
    class Meta:
        verbose_name = '物件空間'
        verbose_name_plural = '物件空間'

    def __str__(self):
        return f'{self.case} - {self.space}'
        
    case = models.ForeignKey(to=Case, on_delete=models.CASCADE, null=True, blank=True, verbose_name='物件')
    space = models.ForeignKey(to=SpaceName, on_delete=models.CASCADE, null=True, blank=True, verbose_name='空間名')
    area = models.FloatField(verbose_name='坪數', null=True, blank=True, )
    note = models.CharField(verbose_name='空間備註', max_length=100, null=True, blank=True)


# class Quotation(models.Model):
#     class Meta:
#         verbose_name = '報價單'
#         verbose_name_plural = '報價單'

#     def __str__(self):
#         return f'{self.case.name} - v{self.version}'

#     case = models.ForeignKey(to=Case, verbose_name='物件', on_delete=models.CASCADE, null=True, blank=False, related_name='quotation')
#     quote_date = models.DateField(verbose_name='報價日期', null=True, blank=True)
#     version = models.PositiveSmallIntegerField(verbose_name='版本', null=True, blank=True)
#     note = models.TextField(verbose_name='備註', null=True, blank=True)


# class QuotationItem(models.Model):
    
#     # def __str__(self):
#     #     return self.work.name

#     class Meta:
#         verbose_name = '報價單內項目'
#         verbose_name_plural = '報價單內項目'
        
#     quotation = models.ForeignKey(Quotation, verbose_name='報價單', on_delete=models.CASCADE, related_name='items')

#     space = ChainedForeignKey(
#         to=SpaceName, verbose_name='空間', null=True, blank=True,
#         chained_field='quotation', chained_model_field='case__quotation',
#         show_all=False, auto_choose=True
#     )

#     layer1 = models.ForeignKey(Layer1, verbose_name='工種', on_delete=models.CASCADE, null=True, blank=True)
    
#     layer2 = ChainedForeignKey(
#         to=Layer2, verbose_name='分類', null=True, blank=True,
#         chained_field='layer1', chained_model_field='layer1',
#         show_all=False, auto_choose=True
#     )
    
#     work = ChainedForeignKey(
#         to=Work, verbose_name='項目', null=True, blank=True,
#         chained_field='layer2', chained_model_field='layer2',
#         show_all=False, auto_choose=True
#     )

#     provider_work = ChainedForeignKey(
#         to=VendorWork, verbose_name='施作廠商', null=True, blank=True,
#         chained_field='work', chained_model_field='work',
#         show_all=False, auto_choose=True
#     )

#     amount = models.SmallIntegerField(
#         '數量', null=True, blank=True, default=0
#     )

#     def price(self):
#         return f'$ {self.amount * self.work.unit_price}' if self.amount else '-'
#     price.short_description = '價格'