from django.contrib import admin
from .models import Battle, Category


# Register your models here.
@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class Category(admin.ModelAdmin):
    pass
