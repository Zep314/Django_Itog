from django.core.management.base import BaseCommand
from ...models import Recipe, Author
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Работа с таблицей рецептов: Создание рецепта
    """
    help = "Create recipe."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Recipe name')
        parser.add_argument('description', type=str, help='Recipe description')
        parser.add_argument('roadmap', type=str, help='Recipe roadmap')
        parser.add_argument('req_time', type=int, help='Recipe required time')
        parser.add_argument('image', type=str, help='Recipe image')
        parser.add_argument('author_id', type=int, help='Recipe author id')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        roadmap = kwargs.get('roadmap')
        req_time = kwargs.get('req_time')
        image = kwargs.get('image')
        author_id = kwargs.get('author_id')

        author = Author.objects.filter(pk=author_id).first()

        recipe = Recipe(name=name, description=description, roadmap=roadmap,
                        req_time=req_time, image=image, author=author)
        recipe.save()
        logger.info(f'Successfully create recipe: {recipe}')
