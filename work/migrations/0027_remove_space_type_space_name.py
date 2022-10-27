# Generated by Django 4.0.5 on 2022-09-21 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0026_spacetype_alter_spacename_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='space',
            name='type',
        ),
        migrations.AddField(
            model_name='space',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.spacename', verbose_name='空間名稱'),
        ),
    ]
