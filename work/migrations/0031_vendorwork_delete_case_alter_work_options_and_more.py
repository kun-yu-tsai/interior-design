# Generated by Django 4.0.5 on 2022-09-21 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0006_alter_providerwork_active'),
        ('work', '0030_alter_layer1_options_alter_layer1_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveSmallIntegerField(null=True, verbose_name='價錢')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.provider', verbose_name='施作廠商')),
            ],
            options={
                'verbose_name': '廠商施作',
                'verbose_name_plural': '廠商施作',
            },
        ),
        migrations.DeleteModel(
            name='Case',
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': '工程項目', 'verbose_name_plural': '工程項目'},
        ),
        migrations.AddField(
            model_name='vendorwork',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='work.work', verbose_name='工程項目'),
        ),
    ]
