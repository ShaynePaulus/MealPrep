from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Recipes(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    directions = models.TextField()
    prep_time_hr = models.IntegerField(blank=True, null=True)
    prep_time_min = models.IntegerField(blank=True, null=True)
    cook_time_hr = models.IntegerField(blank=True, null=True)
    cook_time_min = models.IntegerField(blank=True, null=True)
    total_time = models.IntegerField(blank=True, null=True)
    servings = models.CharField(max_length=255,blank=True, null=True)
    image = models.ImageField(upload_to='recipe_photos', null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=255)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=255, null=True)

class Measurements(models.Model):
    measurement = models.CharField(max_length=255)

class Quantities(models.Model):
    quantity = models.CharField(max_length=255)

class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurements, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Quantities, on_delete=models.CASCADE)

class RecipeTags(models.Model):
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)

class RecipeFavorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)

'''
# recipes/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()

  author = models.ForeignKey(User, on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
'''