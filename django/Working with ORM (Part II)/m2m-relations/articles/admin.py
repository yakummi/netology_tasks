from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Article, Theme, Relations
from django.core.exceptions import ValidationError

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            dictionary = form.cleaned_data
            if not dictionary.get('main'):
                continue
            elif dictionary['main'] is True:
                i += 1
        if i == 0:
            raise ValidationError('Выберите главную тему')
        elif i > 1:
            raise ValidationError('Главной темой может быть только одна')
        return super().clean()

class RelationsInline(admin.TabularInline):
    model = Relations
    formset = RelationshipInlineFormset




@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationsInline]
    save_on_top = True
