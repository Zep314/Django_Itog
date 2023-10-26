from django.shortcuts import render, redirect
import logging
from django.views import View
from .models import Recipe

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    """
    Функция - заглушка. Если вызов был без параметров.
    :param request:
    :return:
    """
    logger.info('Index page accessed! Redirect to /recipes')
    return redirect("/recipes")

class Recipes(View):
    """
    Класс - форма вывода содержимого базы данных по запросу
    """

    def get(self, request):
        """
        :param request: django объект - запрос
        :return:
        """
        recipes = Recipe.objects.all()

        context = { 'recipes': recipes,
                    }
        return render(request, 'website/recipes.html', context)
