# Generated by Django 5.1.3 on 2024-12-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_departments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_type',
            field=models.CharField(choices=[('adult', 'Взрослая'), ('children', 'Детская')], max_length=10, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='department',
            name='location',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Адрес'),
        ),
    ]
