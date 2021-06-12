from rest_framework import routers

from .views import *

app_name = "api_recipes"

router = routers.DefaultRouter()
router.register(r'', RecipeViewSet)
