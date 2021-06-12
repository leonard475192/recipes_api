from django import forms
from .models import *

def get_error_dict(errors):
  error_dict = {}
  for field_name, errors in errors.items():
    error_dict[field_name] = []
    for error in errors:
      error_dict[field_name].append(error)
  return error_dict

class RecipeAPIForm(forms.ModelForm):
  def check_mandatory(self):
    try:
      self.data.get('title')
      self.data.get('making_time')
      self.data.get('serves')
      self.data.get('ingredients')
      self.data.get('cost')
      return True
    except:
      return False

  class Meta:
    model = Recipe
    fields = ('title', 'making_time', 'serves', 'ingredients', 'cost', 'created_at', 'updated_at')