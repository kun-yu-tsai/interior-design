# Generated by Django 4.0.5 on 2022-09-21 09:48

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('space_settings', '0001_initial'),
        ('quotation', '0014_alter_quotationitem_provider_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationitem',
            name='space',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='quotation', chained_model_field='case__quotation', null=True, on_delete=django.db.models.deletion.CASCADE, to='space_settings.spacename', verbose_name='空間'),
        ),
    ]
