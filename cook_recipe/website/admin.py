from django.contrib import admin
from .models import Recipe, Category, Category_Recipe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    """
    Класс для администрирования таблицы категорий
    """
    list_display = ['name']
    ordering = ['name']
    list_filter = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Name'


    fieldsets = [
        (
            'Название категории',
            {
                'classes': 'wide',
                'fields': ['name'],
            }
        ),
    ]

class CategoryRecipeAdmin(admin.ModelAdmin):
    """
    Класс для администрирования таблицы связей категорий и рецептов
    """
    list_display = ['category', 'recipe']
    ordering = ['category', 'recipe']
    list_filter = ['category', 'recipe']
    search_fields = ['category', 'recipe']
    search_help_text = 'Поиск по полям Category и Recipe'

    fieldsets = [
        (
            'Категории',
            {
                'classes': 'wide',
                'fields': ['category'],
            }
        ),
        (
            'Рецепты',
            {
                'classes': 'wide',
                'fields': ['recipe'],
            }
        ),
    ]

class RecipeAdmin(admin.ModelAdmin):
    """
    Класс для администрирования таблицы рецептов
    """
    list_display = ['name', 'description', 'roadmap', 'req_time', 'image', 'author']
    ordering = ['name']
    list_filter = ['name', 'description', 'roadmap', 'req_time', 'image', 'author']
    search_fields = ['name', 'description', 'roadmap', 'req_time', 'image', 'author']
    search_help_text = 'Поиск по всем полям'
    fieldsets = [
        (
            'Описание',
            {
                'classes': 'wide',
                'fields': ['name', 'description'],
            }
        ),
        (
            'Процесс приготовления',
            {
                'classes': 'wide',
                'fields': ['roadmap', 'req_time'],
            }
        ),
        (
            None,
            {
                'classes': 'wide',
                'fields': ['image', 'author'],
            }
        ),
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Category_Recipe, CategoryRecipeAdmin)
admin.site.register(Recipe, RecipeAdmin)
