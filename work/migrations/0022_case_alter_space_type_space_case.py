# Generated by Django 4.0.5 on 2022-08-04 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0021_spacetype_alter_layer1_options_alter_layer2_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='案名')),
                ('case_number', models.CharField(max_length=30, null=True, verbose_name='案號')),
                ('address', models.CharField(max_length=5, null=True, verbose_name='地址')),
                ('owner', models.CharField(max_length=30, null=True, verbose_name='業主')),
                ('contact', models.CharField(max_length=30, null=True, verbose_name='聯絡方式')),
            ],
            options={
                'verbose_name': '案件',
                'verbose_name_plural': '案件',
            },
        ),
        migrations.AlterField(
            model_name='space',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.spacetype', verbose_name='空間類別'),
        ),
        migrations.AddField(
            model_name='space',
            name='case',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='work.case', verbose_name='所屬案件'),
        ),
    ]