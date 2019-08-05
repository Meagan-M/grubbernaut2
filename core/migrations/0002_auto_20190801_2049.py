# Generated by Django 2.2.3 on 2019-08-01 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(related_name='restaurant', through='core.Favorite', to='core.Restaurant'),
        ),
    ]
