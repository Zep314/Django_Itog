from django.core.management.base import BaseCommand
from ...models import Recipe, Category_Recipe, Category

import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    """
    Очистка всех таблиц
    """
    help = "Clear all tables"

    def handle(self, *args, **kwargs):

        category_recipes = Category_Recipe.objects.all()
        for category_recipe in category_recipes:
            category_recipe.delete()
        logger.info('Clear all data in Category_Recipe table!')

        categorys = Category.objects.all()
        for category in categorys:
            category.delete()
        logger.info('Clear all data in Category table!')

        recipes = Recipe.objects.all()
        for recipe in recipes:
            recipe.delete()
        logger.info('Clear all data in Receipe table!')


