# Generated by Django 4.0.5 on 2022-07-03 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='amount',
        ),
    ]
