# Generated by Django 5.1.3 on 2025-01-20 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_aboutuspage_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maindoctorcontent',
            name='image',
        ),
    ]
