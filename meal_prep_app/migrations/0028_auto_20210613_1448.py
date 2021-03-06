# Generated by Django 3.1.7 on 2021-06-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_prep_app', '0027_shoppinglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='amounts',
            field=models.ManyToManyField(blank=True, to='meal_prep_app.Amount'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='recipe_lists',
            field=models.ManyToManyField(blank=True, to='meal_prep_app.RecipeList'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='recipes',
            field=models.ManyToManyField(blank=True, to='meal_prep_app.Recipe'),
        ),
    ]
