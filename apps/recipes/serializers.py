from rest_framework import serializers
from apps.recipes.models import *


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Recipe
        depth = 1

    def create(self, validated_data):
        ingredient_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)

        for ingredient in ingredient_data:
            try:
                ingredient = Ingredient.objects.get(name=ingredient["name"])
            except Ingredient.DoesNotExist:
                ingredient = Ingredient.objects.create(**ingredient)
            recipe.ingredients.add(ingredient)

        return recipe


    def get_comments(self, obj):
        comments = Comment.objects.filter(recipe=obj.id)
        serializer = CommentSerializer(comments, many=True)
        return serializer.data
