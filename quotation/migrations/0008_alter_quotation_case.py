# Generated by Django 4.0.5 on 2022-08-04 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0022_case_alter_space_type_space_case'),
        ('quotation', '0007_remove_quotation_name_quotationitem_case_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='case',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotation', to='work.case', verbose_name='所屬案件'),
        ),
    ]