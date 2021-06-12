from django.db import models
from django.utils import timezone

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(verbose_name="タイトル", max_length=100, blank=False, null=False)
  making_time = models.CharField(verbose_name="調理時間", max_length=100, blank=False, null=False)
  serves = models.CharField(verbose_name="人前", max_length=100, blank=False, null=False)
  ingredients = models.CharField(verbose_name="材料", max_length=300, blank=False, null=False)
  cost = models.IntegerField(verbose_name="値段", blank=False, null=False)
  created_at = models.DateTimeField(verbose_name="登録日時", blank=True, null=False, default=timezone.now)
  updated_at = models.DateTimeField(verbose_name="最終更新日時", blank=True, null=False, default=timezone.now)
