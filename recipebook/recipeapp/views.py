# yourapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer


class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailView(APIView):  # Новое представление для получения конкретной категории
    def get(self, request, id, *args, **kwargs):
        try:
            category = Category.objects.get(id=id)  # Получаем категорию по ID
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category)
        return Response(serializer.data)


class RecipeListView(APIView):
    def get(self, request, *args, **kwargs):
        category_id = request.query_params.get('category')  # Получаем id категории из параметров запроса
        
        if category_id:
            # Фильтруем рецепты по категории, если category_id передан в запросе
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            recipes = Recipe.objects.filter(categories=category)
        else:
            # Если category_id не передан, возвращаем все рецепты
            recipes = Recipe.objects.all()
        
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)


class RecipeDetailView(APIView):  # Новое представление для получения конкретной категории
    def get(self, request, id, *args, **kwargs):
        try:
            recipe = Recipe.objects.get(id=id)  # Получаем категорию по ID
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
