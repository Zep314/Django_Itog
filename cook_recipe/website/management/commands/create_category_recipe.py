from django.core.management.base import BaseCommand
from ...models import Recipe, Category, Category_Recipe
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Работа с таблицей рецептов: Создание рецепта
    """
    help = "Create link between category and recipe."

    def add_arguments(self, parser):
        parser.add_argument('category_id', type=int, help='Category id')
        parser.add_argument('recipe_id', type=int, help='Recipe id')

    def handle(self, *args, **kwargs):
        category_id = kwargs.get('category_id')
        recipe_id = kwargs.get('recipe_id')

        category = Category.objects.filter(pk=category_id).first()
        recipe = Recipe.objects.filter(pk=recipe_id).first()

        category_recipe = Category_Recipe(category=category, recipe=recipe)

        category_recipe.save()
        logger.info(f'Successfully create link between category and recipe: {category_recipe}')
