from django.db import models
from work.models import Layer1, Layer2, VendorWork, Work
from cases.models import Case, CaseSpace
from space_settings.models import SpaceName
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.
class Quotation(models.Model):
    class Meta:
        verbose_name = '報價單'
        verbose_name_plural = '報價單'

    def __str__(self):
        return f'{self.case.name} - v{self.version}'

    case = models.ForeignKey(to=Case, verbose_name='所屬案件', on_delete=models.CASCADE, null=True, blank=False, related_name='quotation')
    discount_code = models.CharField(verbose_name='優惠碼', max_length=30, null=True, blank=True)
    version = models.PositiveSmallIntegerField(verbose_name='版本', null=True, blank=True)
    
    quote_date = models.DateField(verbose_name='報價日期', null=True, blank=True)
    valid_until_date = models.DateField(verbose_name='效期日（包含）', null=True, blank=True)

    design_fee = models.PositiveIntegerField(verbose_name='設計費', null=True, blank=False, default=0)
    supervise_fee = models.PositiveIntegerField(verbose_name='監管費', null=True, blank=False, default=0)
    discount_amount = models.PositiveIntegerField(verbose_name='折扣額', null=True, blank=False, default=0)

    extra_tax_percentage = models.PositiveIntegerField(verbose_name='稅金費率（%）', null=True, blank=False, default=5)

    note = models.TextField(verbose_name='備註', null=True, blank=True)

    def final_price(self):
        price = 0
        
        for item in self.items.all():
            price += item.price()

        price += self.design_fee
        price += self.supervise_fee
        price -= self.discount_amount
        price += price * self.extra_tax_percentage / 100

        return (int)(price)
    final_price.short_description = '總計'



class QuotationItem(models.Model):
    
    def __str__(self):
        return f'{self.quotation}, {self.space_name}, {self.vendor_work}'

    @property
    def space_name(self):
        return self.space.space if self.space else ''

    class Meta:
        verbose_name = '報價單內項目'
        verbose_name_plural = '報價單內項目'
        
    quotation = models.ForeignKey(Quotation, verbose_name='報價單', on_delete=models.CASCADE, related_name='items')

    space = ChainedForeignKey(
        to=CaseSpace, verbose_name='空間', null=True, blank=True,
        chained_field='quotation', chained_model_field='case__quotation',
        show_all=False, auto_choose=True
    )

    layer1 = models.ForeignKey(Layer1, verbose_name='工種', on_delete=models.CASCADE, null=True, blank=True)
    
    layer2 = ChainedForeignKey(
        to=Layer2, verbose_name='分類', null=True, blank=True,
        chained_field='layer1', chained_model_field='layer1',
        show_all=False, auto_choose=True
    )
    
    work = ChainedForeignKey(
        to=Work, verbose_name='項目', null=True, blank=True,
        chained_field='layer2', chained_model_field='layer2',
        show_all=False, auto_choose=True
    )

    vendor_work = ChainedForeignKey(
        to=VendorWork, verbose_name='施作廠商', null=True, blank=True,
        chained_field='work', chained_model_field='work',
        show_all=False, auto_choose=True
    )

    amount = models.SmallIntegerField(
        '數量', null=True, blank=False, default=0
    )

    weighting = models.FloatField(verbose_name='乘數', null=True, blank=False, default=1.2)

    def price_display(self):
        return f'$ {self.amount * self.work.unit_price * self.weighting}' if self.amount else '-'
    price_display.short_description = '價格'

    def price(self):
        print(self)
        print(self.amount)
        print(self.work.unit_price)
        print(self.weighting)
        return self.amount * self.work.unit_price * self.weighting