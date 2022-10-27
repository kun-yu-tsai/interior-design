from django.db import models

# Create your models here.
class SpaceType(models.Model):
    class Meta:
        verbose_name = '空間類型'
        verbose_name_plural = '      空間類型'

    def __str__(self):
        return self.name

    name = models.CharField(
        verbose_name='類型名稱', max_length=20, null=True, blank=False)

class SpaceName(models.Model):
    class Meta:
        verbose_name = '空間名稱'
        verbose_name_plural = '      空間名稱'
   
    def __str__(self):
        return self.name

    type = models.ForeignKey(to=SpaceType, verbose_name='空間類型', on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField(
        verbose_name='空間名稱', max_length=20, null=True, blank=False)