# Generated by Django 4.0.5 on 2022-07-27 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0011_alter_layer1_name_alter_layer2_belong_to_and_more'),
        ('quotation', '0002_quotationitem_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationitem',
            name='layer1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.layer1'),
        ),
        migrations.AddField(
            model_name='quotationitem',
            name='layer2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.layer2'),
        ),
        migrations.AddField(
            model_name='quotationitem',
            name='layer3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.layer3'),
        ),
        migrations.AlterField(
            model_name='quotationitem',
            name='work',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.work'),
        ),
    ]
