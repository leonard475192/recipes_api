from django.urls import path

from .views import *

app_name = "api_recipes"

urlpatterns = [
  # GET:一覧, POST:追加
  path('', recipes, name="all"),
  # GET:特定のレシピ, PATCH:更新, DELETE:削除
  path('<int:pk>', recipe_detail, name="detail"),
]
