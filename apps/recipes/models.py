from django.db import models


class Ingredient(models.Model):
    name = models.TextField(max_length = 100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True, help_text = "This is a quick description of your recipes")
    directions = models.TextField(help_text = "How to make the recipes")
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

class Comment(models.Model):
    body = models.TextField()
    recipe = models.ForeignKey(Recipe)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
