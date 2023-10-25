from django.core.management.base import BaseCommand
from ...models import Author, Recipe, Category_Receipe, Category

import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    """
    Очистка всех таблиц
    """
    help = "Clear all tables"

    def handle(self, *args, **kwargs):

        category_recipes = Category_Receipe.objects.all()
        for category_recipe in category_recipes:
            category_recipe.delete()
        logger.info('Clear all data in Category_Receipe table!')

        categorys = Category.objects.all()
        for category in categorys:
            category.delete()
        logger.info('Clear all data in Category table!')

        recipes = Recipe.objects.all()
        for recipe in recipes:
            recipe.delete()
        logger.info('Clear all data in Receipe table!')

        authors = Author.objects.all()
        for author in authors:
            author.delete()
        logger.info('Clear all data in Author table!')

