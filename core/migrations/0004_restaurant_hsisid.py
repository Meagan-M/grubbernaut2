# Generated by Django 2.2.3 on 2019-08-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190801_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='hsisid',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
