from django.shortcuts import render, redirect
import logging
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Recipe
from .forms import RecipeForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib import messages

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


class Recipes(ListView):
    """
    Класс - форма вывода содержимого базы данных по запросу
    """
    paginate_by = 2
    model = Recipe
    def get(self, request):
        """
        :param request: django объект - запрос
        :return:
        """
        recipes = Recipe.objects.all()
        paginator = Paginator(recipes, 5)

        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {'recipes': recipes,
                   'page_obj': page_obj,
                   }
        # print(f'{context}')
        return render(request, 'website/recipes.html', context)


class RecipeDetail(View):
    def get(self, request):
        """
        Обработка формы при создании нового рецепта
        :param request:
        :return:
        """

        form = RecipeForm(initial={'id': '0',
                                   'name': '',
                                   'description': '',
                                   'roadmap': '',
                                   'req_time': 1,
                                   'image': '',
                                   'old_image': '',
                                   'author_id': request.user.id,
                                   })
        messages.info(request, f'Заполните форму')

        return render(request, 'website/recipe_detail.html', {'form': form})

    def post(self, request):
        """
        Обработка формы при редактировании или сохранении данных
        :param request:
        :return:
        """
        if 'recipe_id' in request.POST:
            # Нажали кнопку РЕДАКТИРОВАТЬ - отображаем форму с редактируемыми данными

            # Вытаскиваем данные из базы данных
            recipe = Recipe.objects.filter(pk=request.POST['recipe_id']).first()
            initial = {'id': str(request.POST['recipe_id']),
                       'name': recipe.name,
                       'description': recipe.description,
                       'roadmap': recipe.roadmap,
                       'req_time': recipe.req_time,
                       'image': recipe.image,
                       'old_image': recipe.image,
                       'author_id': request.user.id
                       }
            form = RecipeForm(initial=initial)
            messages.info(request, f'Измените данные')
            return render(request, 'website/recipe_detail.html', {'form': form})
        else:
            # Пытаемся сохранить данные из формы
            form = RecipeForm(request.POST, request.FILES)

            if form.is_valid():
                recipe_id = form.cleaned_data['id']
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                roadmap = form.cleaned_data['roadmap']
                req_time = form.cleaned_data['req_time']
                image = form.cleaned_data['image']
                old_image = form.cleaned_data['old_image']
                author_id = form.cleaned_data['author_id']
                author = User.objects.filter(pk=author_id).first()
                fs = FileSystemStorage()

                if image:
                    fs.save(image.name, image)

                if recipe_id == 0:
                    # Вновь создаваемый рецепт
                    recipe = Recipe(name=name, description=description,
                                    roadmap=roadmap, req_time=req_time, image=image.name, author=author)
                else:
                    # Изменение данных уже существующего рецепта
                    recipe = Recipe.objects.filter(pk=recipe_id).first()
                    recipe.name = name
                    recipe.description = description
                    recipe.roadmap = roadmap
                    recipe.req_time = req_time
                    recipe.image = image.name if image else old_image
                    recipe.author = author
                recipe.save()
                logger.info(f'Successfully create recipe: {recipe}')
                return redirect("/")  # Переходим к таблице рецептов
            else:
                # если ошибка (или валидация не пройдена) - заново отображаем форму, с уже заполненными данными
                messages.warning(request, f'Ошибка в данных')
                return render(request, 'website/recipe_detail.html', {'form': form})


class RecipeDelete(View):
    def post(self, request):
        if 'recipe_id' in request.POST:
            # Нажали кнопку УДАЛИТЬ - отображаем форму с подтверждением удаления

            recipe = Recipe.objects.filter(pk=request.POST['recipe_id']).first()
            messages.info(request, f'Подтверждение удаления')
            return render(request, 'website/recipe_delete.html',
                          {'recipe_id': str(request.POST['recipe_id']),
                           'recipe': recipe,
                           })
        else:
            # Подтвердили удаление в форме
            recipe_id = request.POST['id']
            recipe = Recipe.objects.filter(pk=recipe_id).first()
            if recipe is not None:
                logger.info(f'Successfully delete recipe (id={recipe_id}): {recipe}')
                recipe.delete()
            else:
                logger.warning(f'Client (id={recipe_id}) don\'t exist!')
            return redirect("/")
