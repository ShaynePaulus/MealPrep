from .models import RecipeIngredients, Ingredients, Measurements, Quantities

def saverecipeingredients(data, recipe):
    i = m = q = None
    for key, value in data.items():
            if 'ingredient' in key and value:
                i = Ingredients.objects.get_or_create(ingredient=value.title())
            if 'measurement' in key and value:
                m = Measurements.objects.get_or_create(measurement=value.title())
            if 'quantity' in key and value:
                q = Quantities.objects.get_or_create(quantity=value.title())
            if i and m and q:
                RecipeIngredients.objects.create(recipe=recipe, ingredient=i[0], measurement=m[0], quantity=q[0])
                i = m = q = None
        
