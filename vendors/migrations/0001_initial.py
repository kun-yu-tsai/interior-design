# Generated by Django 4.0.5 on 2022-09-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='廠商名稱')),
                ('address', models.CharField(max_length=20, null=True, verbose_name='地址')),
                ('tax_number', models.CharField(max_length=20, null=True, verbose_name='統編')),
                ('contact_person', models.CharField(max_length=20, null=True, verbose_name='聯絡人')),
                ('contact_number', models.CharField(max_length=20, null=True, verbose_name='聯絡電話')),
            ],
            options={
                'verbose_name': '廠商',
                'verbose_name_plural': '廠商',
            },
        ),
    ]
