# Generated by Django 3.0.2 on 2020-01-14 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PCHelp', '0002_bid_datecreation'),
    ]

    operations = [
        migrations.AddField(
            model_name='сomment',
            name='datecreation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
