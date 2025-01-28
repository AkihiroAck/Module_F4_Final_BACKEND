from rest_framework import serializers
from .models import Category, Recipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)  # Вложенный сериализатор для категорий

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'categories']
