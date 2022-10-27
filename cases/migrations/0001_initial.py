# Generated by Django 4.0.5 on 2022-09-21 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('space_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='物件名稱')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='物件地址')),
                ('total_area', models.FloatField(blank=True, null=True, verbose_name='總坪數')),
            ],
            options={
                'verbose_name': '物件',
                'verbose_name_plural': '物件',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='客戶名稱')),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='聯繫電話')),
            ],
            options={
                'verbose_name': '客戶',
                'verbose_name_plural': '客戶',
            },
        ),
        migrations.CreateModel(
            name='CaseSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField(blank=True, null=True, verbose_name='坪數')),
                ('note', models.CharField(blank=True, max_length=100, null=True, verbose_name='空間備註')),
                ('case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.case', verbose_name='物件')),
                ('space', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='space_settings.spacename', verbose_name='空間名')),
            ],
            options={
                'verbose_name': '物件空間',
                'verbose_name_plural': '物件空間',
            },
        ),
        migrations.AddField(
            model_name='case',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.customer', verbose_name='客戶'),
        ),
    ]
