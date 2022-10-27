from django.db import models
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField

from vendors.models import Vendor


class Unit(models.Model):
    class Meta:
        verbose_name = '單位'
        verbose_name_plural = '單位'

    def __str__(self):
        return self.name

    name = models.CharField(
        verbose_name='單位', max_length=5, null=True, blank=False)


class Layer1(models.Model):
    class Meta:
        verbose_name = '工種名稱'
        verbose_name_plural = '      工種名稱'

    def __str__(self):
        return f'{self.name}'

    name = models.CharField(
        verbose_name='工種名稱', max_length=20, null=True, blank=True)
    # photo = models.ImageField(
    #     upload_to='cate1_picture', null=True, blank=True, verbose_name='圖片檔案', help_text="長寬：200x200")
    # ordering = models.PositiveSmallIntegerField('顯示順序', default=0)


class Layer2(models.Model):
    class Meta:
        verbose_name = ' 工種分類'
        verbose_name_plural = '    工種分類'

    def __str__(self):
        return f'{self.layer1} - {self.name}'

    name = models.CharField(
        verbose_name='名稱', max_length=20, null=True, blank=False)
    layer1 = models.ForeignKey(
        to=Layer1, on_delete=models.CASCADE, verbose_name='所屬工程', null=True, blank=True, )
    # photo = models.ImageField(
    #     upload_to='cate1_picture', null=True, blank=True, verbose_name='圖片檔案', help_text="長寬：200x200")
    # ordering = models.PositiveSmallIntegerField('顯示順序', default=0)



class Work(models.Model):
    class Meta:
        verbose_name = '工程項目'
        verbose_name_plural = '工程項目'

    def __str__(self):
        return f'{self.name} - ${self.unit_price}/{self.unit}'

    name = models.CharField(
        verbose_name='項目名稱', max_length=20, null=True, blank=False)
    layer2 = models.ForeignKey(
        to=Layer2, on_delete=models.CASCADE, verbose_name='工種分類', null=True, blank=True,
        # chained_field='layer1', chained_model_field='layer1',
        # show_all=False, auto_choose=True
    )
    # layer2 = models.ForeignKey(
    #     to=Layer2, verbose_name='第二層', on_delete=models.CASCADE, null=True, blank=True, )
    # layer3 = models.ForeignKey(
    #     to=Layer3, verbose_name='第三層', on_delete=models.CASCADE, null=True, blank=True, )
    unit = models.ForeignKey(to=Unit, verbose_name='單位',
                             on_delete=models.CASCADE, null=True, blank=True, )

    unit_price = models.PositiveSmallIntegerField(
        verbose_name='單價', null=True, blank=True, default=100)
    # weighting = models.FloatField('乘數', null=True, blank=True, default=1.2)


class VendorWork(models.Model):
    class Meta:
        verbose_name = '廠商施作項目'
        verbose_name_plural = '廠商施作項目'

    def __str__(self):
        return f'{self.work} - {self.vendor}:${self.price}'


    work = models.ForeignKey(
        to=Work, on_delete=models.CASCADE, verbose_name='工程項目', null=True, blank=True, )
    vendor = models.ForeignKey(
        to=Vendor, on_delete=models.CASCADE, verbose_name='施作廠商', null=True, blank=True, )
    price = models.PositiveSmallIntegerField(
        verbose_name='價錢', null=True, blank=False)