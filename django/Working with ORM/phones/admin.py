from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exist', 'slug']

