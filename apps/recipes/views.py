from django.shortcuts import render
from rest_framework import generics
from apps.recipes.serializers import *


# Create your views here.
class RecipeList(generics.ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
