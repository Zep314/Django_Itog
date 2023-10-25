from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    """
    Описываем модель данных для работы с таблицей рецептов
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    roadmap = models.CharField(max_length=255, blank=True, null=True)
    req_time = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    image = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: \'{self.name}\', Description: \'{self.description}\', Roadmap: \'{self.roadmap}\', ' \
               f'Required time: {self.req_time}, Image: {self.image}, Author: {self.author}'


class Category(models.Model):
    """
    Описываем модель данных для работы с таблицей категорий
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'Name: \'{self.name}\''

class Category_Recipe(models.Model):
    """
    Описываем модель данных для работы с таблицей связей категории и рецепта
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
