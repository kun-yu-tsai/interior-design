# Generated by Django 4.0.5 on 2022-07-28 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0013_remove_work_layer2_work_layer2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='layer2',
            old_name='belong_to',
            new_name='layer1',
        ),
        migrations.RenameField(
            model_name='layer3',
            old_name='belong_to',
            new_name='layer2',
        ),
    ]
