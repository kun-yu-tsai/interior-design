# Generated by Django 4.0.5 on 2022-07-28 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0016_delete_provider_alter_unit_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='layer2',
            name='layer1',
        ),
        migrations.AddField(
            model_name='layer2',
            name='layer1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.layer1', verbose_name='所屬第一層'),
        ),
    ]
