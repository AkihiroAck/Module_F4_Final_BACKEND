from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'id: {self.pk}, name: {self.name}'
    
    
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='recipes')

    def __str__(self):
        return f'id: {self.pk}, title: {self.title}'
