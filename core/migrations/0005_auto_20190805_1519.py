# Generated by Django 2.2.3 on 2019-08-05 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_restaurant_hsisid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='hsisid',
            new_name='permitid',
        ),
    ]