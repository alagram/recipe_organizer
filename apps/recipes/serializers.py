from rest_framework import serializers
from apps.recipes.models import *


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        depth = 1
