import datetime
import json
import pytz

from django.http.response import JsonResponse
from django.shortcuts import render,  get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import RecipeAPIForm, get_error_dict
from .models import Recipe
from .serializer import RecipeSerializer

jst = pytz.timezone('Asia/Tokyo')

@csrf_exempt
def recipes(request):
    if request.method == "POST":
        try: 
            params = json.loads(request.body)
            params['cost'] = int(params['cost'])
            form = RecipeAPIForm(params)

            if not form.is_valid() or not form.check_mandatory():
                return JsonResponse({
                    "message": "Recipe creation failed!",
                    "required": "title, making_time, serves, ingredients, cost"
                }, status=400)

            recipe = form.save()

            return JsonResponse({
                "message": "Recipe successfully created!",
                "recipe": [{
                    "id": recipe.id,
                    "title": recipe.title,
                    "making_time": recipe.making_time,
                    "serves": recipe.serves,
                    "ingredients": recipe.ingredients,
                    "cost": str(recipe.cost),
                    "created_at": recipe.created_at.astimezone(jst).strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": recipe.updated_at.astimezone(jst).strftime("%Y-%m-%d %H:%M:%S")
                }]
            }, status=201)
        except:
            return JsonResponse({
                "message": "Recipe creation failed!",
                "required": "title, making_time, serves, ingredients, cost"
            }, status=400)
    else:
        recipes = Recipe.objects.all()
        recipes_lst = []
        for recipe in recipes:
            recipe_dict = {
                "id": recipe.id,
                "title": recipe.title,
                "making_time": recipe.making_time,
                "serves": recipe.serves,
                "ingredients": recipe.ingredients,
                "cost": str(recipe.cost),
                "created_at": recipe.created_at.astimezone(jst).strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": recipe.updated_at.astimezone(jst).strftime("%Y-%m-%d %H:%M:%S")
            }
            recipes_lst.append(recipe_dict)
        return JsonResponse({
            "recipes": recipes_lst
        })


@csrf_exempt
def recipe_detail(request, pk):
    try:
        recipe = Recipe.objects.get(id=pk)
        if request.method == "PATCH":
            try: 
                params = json.loads(request.body)
                params['cost'] = int(params['cost'])
                form = RecipeAPIForm(params)

                if not form.is_valid() or not form.check_mandatory():
                    return JsonResponse({
                        "message": "Recipe creation failed!",
                        "required": "title, making_time, serves, ingredients, cost"
                    }, status=400)

                recipe = form.save()

                return JsonResponse({
                    "message": "Recipe successfully updated!",
                    "recipe": [{
                        "title": recipe.title,
                        "making_time": recipe.making_time,
                        "serves": recipe.serves,
                        "ingredients": recipe.ingredients,
                        "cost": str(recipe.cost),
                    }]
                }, status=200)
            except:
                return JsonResponse({
                    "message": "Recipe creation failed!",
                    "required": "title, making_time, serves, ingredients, cost"
                }, status=400)
        elif request.method == "DELETE":
            recipe.delete()
            return JsonResponse({"message": "Recipe successfully removed!"}, status=204)
        else:
            return JsonResponse({
                "message": "Recipe details by id",
                "recipe": [{
                    "id": recipe.id,
                    "title": recipe.title,
                    "making_time": recipe.making_time,
                    "serves": recipe.serves,
                    "ingredients": recipe.ingredients,
                    "cost": str(recipe.cost),
                    }]
                })
    except:
        return JsonResponse({"message":"No Recipe found"}, status=400)
