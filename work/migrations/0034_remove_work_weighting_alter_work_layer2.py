# Generated by Django 4.0.5 on 2022-09-21 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0033_alter_vendorwork_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='weighting',
        ),
        migrations.AlterField(
            model_name='work',
            name='layer2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.layer2', verbose_name='工種分類'),
        ),
    ]
