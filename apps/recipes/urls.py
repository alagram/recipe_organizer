from django.conf.urls import patterns, include, url
from apps.recipes.views import *

urlpatterns = patterns('',
    url(r'^recipes/$', RecipeList.as_view(), name='recipes-list'),
    url(r'^recipes/(?P<pk>[0-9]+)$', RecipeDetail.as_view(), name='recipe-list'),
    url(r'^add-recipe$', AddRecipe.as_view(), name='add-recipe'),
    url(r'^recipes/(?P<pk>[0-9]+)/comments/$', AddComment.as_view(), name='add-comment'),
)
