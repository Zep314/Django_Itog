from django import forms


class RecipeForm(forms.Form):
    """
    Класс - представление для формы создания/редактирования рецепта
    """
    id = forms.IntegerField(widget=forms.HiddenInput())

    name = forms.CharField(max_length=100,
                           label='Наименование рецепта',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название рецепта',
                                                         }))
    description = forms.CharField(max_length=255,
                                  label='Описание рецепта',
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Описание рецепта',
                                                               }))
    roadmap = forms.CharField(max_length=255,
                              label='Шаги приготовления',
                              widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': 'Шаги приготовления рецепта',
                                                           }))
    req_time = forms.IntegerField(min_value=1,
                                  label='Время приготовления',
                                  widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Изображение', required=False)
    old_image = forms.CharField(widget=forms.HiddenInput())
    author_id = forms.IntegerField(widget=forms.HiddenInput())
