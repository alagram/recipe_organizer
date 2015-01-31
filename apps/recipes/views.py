from django.shortcuts import render
from rest_framework import generics
from apps.recipes.serializers import *

class RecipeList(generics.ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class AddRecipe(generics.CreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class AddComment(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
