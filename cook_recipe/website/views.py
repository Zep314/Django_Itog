from django.shortcuts import render, redirect
import logging
from django.views import View

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    """
    Функция - заглушка. Если вызов был без параметров.
    :param request:
    :return:
    """
    logger.info('Index page accessed! Redirect to /lastday/0/7')
    return redirect("/home")

class Home(View):
    """
    Класс - форма вывода содержимого базы данных по запросу
    """

    def get(self, request):
        """
        :param request: django объект - запрос
        :return:
        """

        context = {}
        return render(request, 'website/recipes.html', context)
