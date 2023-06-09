# Generated by Django 4.1.7 on 2023-03-31 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=255)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Quantities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('directions', models.TextField()),
                ('prep_time_hr', models.IntegerField(blank=True, null=True)),
                ('prep_time_min', models.IntegerField(blank=True, null=True)),
                ('cook_time_hr', models.IntegerField(blank=True, null=True)),
                ('cook_time_min', models.IntegerField(blank=True, null=True)),
                ('servings', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipe_photos')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.recipes')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.ingredients')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.measurements')),
                ('quantity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.quantities')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.recipes')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeFavorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.recipes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
