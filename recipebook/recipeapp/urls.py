from django.urls import path
from .views import CategoryListView, CategoryDetailView, RecipeListView, RecipeDetailView

urlpatterns = [
    path('api/category/', CategoryListView.as_view(), name='category-list'),
    path('api/category/<int:id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('api/recipe/', RecipeListView.as_view(), name='recipe-list'),
    path('api/recipe/<int:id>/', RecipeDetailView.as_view(), name='recipe-detail'),
]