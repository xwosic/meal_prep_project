# Generated by Django 3.1.7 on 2021-06-14 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_prep_app', '0029_auto_20210614_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amount',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_pk', to='meal_prep_app.recipe'),
        ),
    ]
