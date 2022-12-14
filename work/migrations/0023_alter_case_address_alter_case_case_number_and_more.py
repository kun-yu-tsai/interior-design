# Generated by Django 4.0.5 on 2022-08-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0022_case_alter_space_type_space_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='address',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='案號'),
        ),
        migrations.AlterField(
            model_name='case',
            name='contact',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='聯絡方式'),
        ),
        migrations.AlterField(
            model_name='case',
            name='owner',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='業主'),
        ),
    ]
