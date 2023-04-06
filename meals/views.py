from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.forms import formset_factory

from .forms import RecipeForm, RecipeIngredientsForm, IngredientFormSet, RecipeUrlForm
from .models import Recipes, RecipeIngredients, Ingredients, Measurements, Quantities, RecipeTags
from .utils import saverecipeingredients

from recipe_scrapers import scrape_me

import re

# Create your views here.
class Menu(View):
    def get(self, request):
        return HttpResponse('Home')

class RecipesView(ListView):
        model = Recipes
        paginate_by = 12
        

class Recipe(View):
    def get(self, request, pk):
        recipe = Recipes.objects.get(pk=pk)
        ingredients = RecipeIngredients.objects.filter(recipe_id=pk)
        context = {'recipe': recipe, 'ingredients':ingredients}
        return render(request, 'meals/recipe.html', context)

class RecipeUrlCreate(View):
    def get(self, request):
        form = RecipeUrlForm()
        context = {'form': form}
        return render(request, 'meals/recipe_url_form.html', context)
    def post(self, request):
        form = RecipeUrlForm(request.POST)
        if not form.is_valid():
            context = {'form': form}
            return render(request, 'meals/recipe_url_form.html', context)

        new_recipe = Recipes()

        url = form.cleaned_data['url']
        scraper = scrape_me(url)


        new_recipe.title = scraper.title()
        new_recipe.author = request.user
        new_recipe.url = url
        # category = 
        # description = 
        new_recipe.directions = scraper.instructions()
        new_recipe.total_time = scraper.total_time()
        new_recipe.servings = scraper.yields()
        new_recipe.image_url = scraper.image()
        new_recipe.save()
        # tags
        # nutrients = scraper.nutrients()


        #add ingreidents to RecipeIngredients
        for x in scraper.ingredients():
            #print(x)
            match = re.search(r'\d[\d\s /]*(?=\s*[a-zA-Z])', x)
            if match:
                number = match.group()
                item = x[match.end():].strip()
                print(number)
                print(item)
            data = {}
            data['quantity'] = (x.split()[0])
            data['measurement'] = (x.split()[1])
            ingredient = (x.split()[2:])
            data['ingredient'] = ' '.join(ingredient)
            saverecipeingredients(data, new_recipe)
            


        #return HttpResponse('working')
        return redirect(reverse_lazy('meals:recipe-view', args=[new_recipe.id]))

class RecipeCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = RecipeForm()
        formset = IngredientFormSet()
        context = {'form': form, 'formset': formset}
        return render(request, 'meals/recipe_form.html', context)

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES)
        formset = IngredientFormSet(self.request.POST)
        
        if not form.is_valid():
            context = {'form': form, 'formset': formset}
            return render(request, 'meals/recipe_form.html', context)
        
        new_recipe = form.save(commit=False)
        new_recipe.author = request.user
        new_recipe.save()
        
        data = formset[0].data.dict()
        saverecipeingredients(data, new_recipe)
        return redirect(reverse_lazy('meals:recipe-view', args=[new_recipe.id]))

class RecipeUpdate(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipes, pk=pk)
        form = RecipeForm(instance=recipe)
        ingredients = RecipeIngredients.objects.filter(recipe=pk)

        IngredientFormSet = formset_factory(RecipeIngredientsForm, extra=0)
        formset = IngredientFormSet(initial=[{'ingredient': ingredient.ingredient.ingredient, 'quantity': ingredient.quantity.quantity ,'measurement': ingredient.measurement.measurement} for ingredient in ingredients])
        
        context = {'form': form, 'formset': formset}
        return render(request, 'meals/recipe_form.html', context)
        return HttpResponse('RecipeEdit')

    def post(self, request, pk):
        recipe = get_object_or_404(Recipes, pk=pk)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        formset = IngredientFormSet(self.request.POST)
        if not form.is_valid():
            context = {'form': form, 'formset': formset}
            return render(request, 'meals/recipe_form.html', context)
        #add author
        recipe = form.save(commit=False)
        recipe.author = request.user
        recipe.save()
        #remove old ingredients
        RecipeIngredients.objects.filter(recipe=recipe).delete()
        data = formset[0].data.dict()
        saverecipeingredients(data, recipe)
        return redirect(reverse_lazy('meals:recipe-view', args=[recipe.id]))

class RecipeDelete(View):
    def get(self, request, pk):
        recipe = Recipes.objects.get(pk=pk)
        ingredients = RecipeIngredients.objects.filter(recipe_id=pk)
        context = {'recipe': recipe, 'ingredients': ingredients, 'delete': True}
        return render(request, 'meals/recipe.html', context)
    def post(self, request, pk):
        Recipes.objects.get(pk=pk).delete()
        return redirect(reverse_lazy('meals:recipes'))

class GroceryList(View):
    def get(self, request):
        return HttpResponse('GroceryList')
