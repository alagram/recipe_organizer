from django.contrib import admin
from apps.recipes.models import Recipe, Ingredient

admin.site.register(Recipe)
admin.site.register(Ingredient)
