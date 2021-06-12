import django_filters
from rest_framework import viewsets, filters

from django.shortcuts import render

from .models import Recipe
from .serializer import RecipeSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
