# Generated by Django 4.0.5 on 2022-08-04 10:42

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0023_alter_case_address_alter_case_case_number_and_more'),
        ('quotation', '0008_alter_quotation_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotationitem',
            name='case',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='quotation', chained_model_field='quotation', null=True, on_delete=django.db.models.deletion.CASCADE, to='work.case', verbose_name='案件'),
        ),
    ]
