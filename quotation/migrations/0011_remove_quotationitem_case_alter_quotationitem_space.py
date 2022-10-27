# Generated by Django 4.0.5 on 2022-08-04 10:51

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0023_alter_case_address_alter_case_case_number_and_more'),
        ('quotation', '0010_alter_quotationitem_space'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotationitem',
            name='case',
        ),
        migrations.AlterField(
            model_name='quotationitem',
            name='space',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='quotation__case', chained_model_field='case', null=True, on_delete=django.db.models.deletion.CASCADE, to='work.space', verbose_name='空間'),
        ),
    ]