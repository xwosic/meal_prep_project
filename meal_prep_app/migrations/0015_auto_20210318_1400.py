# Generated by Django 3.1.7 on 2021-03-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_prep_app', '0014_auto_20210318_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='amount',
            field=models.FloatField(default=0.0, help_text='Amount of ingredient'),
        ),
    ]
