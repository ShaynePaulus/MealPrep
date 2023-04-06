from django import forms
from django.forms import ModelForm
from meals.models import Recipes, RecipeIngredients
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.forms import formset_factory

class RecipeForm(ModelForm):
    class Meta:
        model = Recipes
        fields = '__all__'
        exclude = ('author',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['prep_time_hr'].label = ""
        self.fields['prep_time_min'].label = ""
        self.fields['cook_time_hr'].label = ""
        self.fields['cook_time_min'].label = ""

class RecipeIngredientsForm(forms.Form):
    ingredient = forms.CharField(max_length=100, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Name of ingredient'}))
    measurement = forms.CharField(max_length=100, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Cup, Tbs...'}))
    quantity = forms.FloatField(required=False,
                                widget=forms.TextInput(attrs={'placeholder': '1,2,3...'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False

IngredientFormSet = formset_factory(RecipeIngredientsForm, extra=1)
        
class RecipeUrlForm(forms.Form):
    url = forms.URLField()